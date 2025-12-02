
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
# F7 chord: F, A, C, E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F (1st beat)
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25), # G (2nd beat)
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625), # E (3rd beat)
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # F (4th beat)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # A (1st beat)
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75), # G (2nd beat)
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.125), # B (3rd beat)
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # A (4th beat)
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # C (1st beat)
    pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.25), # B (2nd beat)
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625), # D (3rd beat)
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # C (4th beat)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4 (1.5 - 6.0s)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1.5, 3.0, 4.5]:
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=bar, end=bar + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=bar + 0.75, end=bar + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=bar + 1.125, end=bar + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=bar + 1.875, end=bar + 2.25))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar + i*0.375, end=bar + i*0.375 + 0.1875))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, C, G (F - Bb - C - G), played over bars 2-4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
