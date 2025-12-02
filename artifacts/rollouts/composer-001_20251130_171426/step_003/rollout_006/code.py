
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625), # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625), # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),  # Ab
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb) on beat 2
    pretty_midi.Note(velocity=95, pitch=53, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625), # Ab

    # Bar 3: Bb7 (Bb, D, F, Ab) on beat 2
    pretty_midi.Note(velocity=95, pitch=50, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75), # Ab

    # Bar 4: Fm7 (F, Ab, C, Eb) on beat 2
    pretty_midi.Note(velocity=95, pitch=53, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25), # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Gb, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=105, pitch=47, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=2.0, end=2.25),  # Gb
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=105, pitch=47, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=3.5, end=3.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=53, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=105, pitch=47, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=5.0, end=5.25),  # Gb
    pretty_midi.Note(velocity=110, pitch=53, start=5.25, end=5.5),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue hihat on every eighth, kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
