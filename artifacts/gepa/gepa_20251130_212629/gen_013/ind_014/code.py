
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Add drum notes
for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=54, start=1.5, end=1.75),  # Fm root (F)
    pretty_midi.Note(velocity=90, pitch=55, start=1.75, end=2.0),  # Gb (chromatic)
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=2.75, end=3.0),  # Bb

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=47, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=4.25, end=4.5),  # D

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=41, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=39, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=5.75, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # Eb

    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # Eb

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # Eb

    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # Eb

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # A (Fm7)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # G (Fm7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F (Fm7)
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # A (Fm7)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F (F7)
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # G (F7)
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # A (F7)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F (F7)
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # A (F7)
]

for note in sax_notes:
    sax.notes.append(note)

# Add drum notes for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on every 8th
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25)

    drums.notes.append(kick1)
    drums.notes.append(snare2)
    drums.notes.append(kick3)
    drums.notes.append(snare4)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)
    drums.notes.append(hihat6)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
