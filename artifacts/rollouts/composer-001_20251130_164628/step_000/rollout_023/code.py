
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line, chromatic approaches, no repeating notes
# D minor key: D, Eb, F, G, Ab, Bb, B
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0),  # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# G7 = G, B, D, F
# Cm7 = C, Eb, G, Bb
# F7 = F, A, C, Eb
piano_notes = [
    # Bar 2 (comp on beat 2)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    # Bar 3 (comp on beat 4)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # B
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),   # F
    # Bar 4 (comp on beat 2)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - short motif, make it sing
# D, F, G, Bb - a questioning phrase
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),   # Bb
    # Rest for a beat
    # Repeat the phrase again to finish the 4 bars
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),   # Bb
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
