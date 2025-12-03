
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

# Drums in bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D5
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # F#5
]

sax.notes.extend(sax_notes)

# Bass: Walking line in D (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),   # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),   # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.5),   # F#2 (chromatic approach)
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),   # G (D7sus4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),   # F#
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0),   # A
]

piano.notes.extend(piano_notes_bar2)

# Drums in bar 2
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes_bar2:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif
sax_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # D5 (repeat motif)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),   # F#5
]

sax.notes.extend(sax_notes_bar3)

# Bass: Walking line
bass_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.25),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5),   # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.75),   # G2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.0),   # F#2 (chromatic approach)
]

bass.notes.extend(bass_notes_bar3)

# Piano: Different chord
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),   # G (D7sus4)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),   # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),   # F#
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.5),   # B (D7sus4 resolved)
]

piano.notes.extend(piano_notes_bar3)

# Drums in bar 3
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes_bar3:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # D5
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),   # F#5
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # D5 (repeat motif)
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),   # F#5
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),   # D5
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),   # F#5 (resolve)
]

sax.notes.extend(sax_notes_bar4)

# Bass: Walking line
bass_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.75),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.75, end=5.0),   # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.25),   # G2
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.5),   # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.5, end=5.75),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=5.75, end=6.0),   # E2 (chromatic approach)
]

bass.notes.extend(bass_notes_bar4)

# Piano: Resolved chord
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),   # G (D7sus4)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),   # F#
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),   # A
]

piano.notes.extend(piano_notes_bar4)

# Drums in bar 4
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes_bar4:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
