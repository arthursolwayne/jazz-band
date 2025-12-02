
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line, chromatic approaches, never the same note twice
# F minor key, walking bass line in F minor
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0), # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75), # D#
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5), # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0), # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
# F7, Bb7, E7, A7
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875), # G
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375), # G
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G, Ab, A, F
# Bar 2: F, G, Ab
# Bar 3: A, F
# Bar 4: (repeat or resolve)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=1.95), # G
    pretty_midi.Note(velocity=110, pitch=73, start=1.95, end=2.15), # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=2.15, end=2.35), # A
    pretty_midi.Note(velocity=110, pitch=74, start=2.35, end=2.55), # F
    pretty_midi.Note(velocity=110, pitch=77, start=2.55, end=2.75), # A
    pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=2.95), # F
    pretty_midi.Note(velocity=110, pitch=76, start=2.95, end=3.15), # G
    pretty_midi.Note(velocity=110, pitch=73, start=3.15, end=3.35), # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=3.35, end=3.55), # A
    pretty_midi.Note(velocity=110, pitch=74, start=3.55, end=3.75), # F
    pretty_midi.Note(velocity=110, pitch=77, start=3.75, end=3.95), # A
    pretty_midi.Note(velocity=110, pitch=74, start=3.95, end=4.15), # F
    pretty_midi.Note(velocity=110, pitch=76, start=4.15, end=4.35), # G
    pretty_midi.Note(velocity=110, pitch=73, start=4.35, end=4.55), # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=4.55, end=4.75), # A
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=4.95), # F
    pretty_midi.Note(velocity=110, pitch=77, start=4.95, end=5.15), # A
    pretty_midi.Note(velocity=110, pitch=74, start=5.15, end=5.35), # F
    pretty_midi.Note(velocity=110, pitch=76, start=5.35, end=5.55), # G
    pretty_midi.Note(velocity=110, pitch=73, start=5.55, end=5.75), # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=5.75, end=5.95), # A
    pretty_midi.Note(velocity=110, pitch=74, start=5.95, end=6.0), # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
