
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # C3
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),   # C3
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # D3
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125),  # C#3
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.5),   # F3
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),   # F3
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # G3
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625),  # F#3
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),   # C4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F5
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # A5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C6
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # G5
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # Bb5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C6
]
# Bar 4: C7 (C, E, G, B)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),   # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),   # F5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # A5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # C6
]
for note in piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - F (sax in F, so Bb is played as Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # F5
    pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=2.0),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25),  # F5
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # F5
    pretty_midi.Note(velocity=110, pitch=61, start=2.75, end=3.0),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # F5
    pretty_midi.Note(velocity=110, pitch=61, start=3.25, end=3.5),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # F5
    pretty_midi.Note(velocity=110, pitch=61, start=3.75, end=4.0),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25),  # F5
    pretty_midi.Note(velocity=110, pitch=61, start=4.25, end=4.5),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75),  # F5
    pretty_midi.Note(velocity=110, pitch=61, start=4.75, end=5.0),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25),  # F5
    pretty_midi.Note(velocity=110, pitch=61, start=5.25, end=5.5),  # Bb4
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.75),  # F5
    pretty_midi.Note(velocity=110, pitch=61, start=5.75, end=6.0),  # Bb4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Fill the bar
# Bar 2: Kick on 1, snare on 2, hihat on every eighth
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + 0.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i * 0.375 + 0.375, end=1.5 + i * 0.375 + 0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + 0.375)
for i in range(3):
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 0.375 + 0.75, end=1.5 + i * 0.375 + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i * 0.375 + 1.125, end=1.5 + i * 0.375 + 1.25)
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i * 0.375 + 0.75, end=1.5 + i * 0.375 + 1.125)

# Bar 3: Kick on 1, snare on 2, hihat on every eighth
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=2.25 + i * 0.375, end=2.25 + i * 0.375 + 0.125),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25 + i * 0.375 + 0.375, end=2.25 + i * 0.375 + 0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25 + i * 0.375, end=2.25 + i * 0.375 + 0.375)
for i in range(3):
    pretty_midi.Note(velocity=100, pitch=36, start=2.25 + i * 0.375 + 0.75, end=2.25 + i * 0.375 + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=2.25 + i * 0.375 + 1.125, end=2.25 + i * 0.375 + 1.25)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25 + i * 0.375 + 0.75, end=2.25 + i * 0.375 + 1.125)

# Bar 4: Kick on 1, snare on 2, hihat on every eighth
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i * 0.375 + 0.375, end=3.0 + i * 0.375 + 0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.375)
for i in range(3):
    pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i * 0.375 + 0.75, end=3.0 + i * 0.375 + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i * 0.375 + 1.125, end=3.0 + i * 0.375 + 1.25)
    pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i * 0.375 + 0.75, end=3.0 + i * 0.375 + 1.125)

midi.instruments.extend([sax, bass, piano, drums])
