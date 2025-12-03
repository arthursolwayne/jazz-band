
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
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
# Hihat on every eighth note
for i in range(4):
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375, end=i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with roots and fifths, D2-G2 (MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: Motif - Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with roots and fifths, D2-G2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G B D F#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5),  # F#4
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),   # E4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
# Hihat on every eighth
for i in range(4):
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line with roots and fifths, D2-G2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),   # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: D7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # C#4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # A4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.75))
# Hihat on every eighth
for i in range(4):
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i * 0.375, end=4.5 + i * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
