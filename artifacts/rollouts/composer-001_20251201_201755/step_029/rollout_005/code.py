
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
drum_notes = []
# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
# Hi-hats on every eighth
for i in range(8):
    start = i * 0.375
    end = start + 0.125
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.75, end=2.0),  # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.25),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=3.25, end=3.5),  # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.75),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # C4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.75),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.75, end=5.0),  # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.25),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.5),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drum_notes = []
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5))
for i in range(8):
    start = 1.5 + i * 0.375
    end = start + 0.125
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 3: 3.0 - 4.5s
drum_notes = []
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
for i in range(8):
    start = 3.0 + i * 0.375
    end = start + 0.125
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 4: 4.5 - 6.0s
drum_notes = []
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5))
for i in range(8):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
