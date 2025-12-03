
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
# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble (1.5 - 3.0s)

# Bass: D2 (MIDI 38), G2 (MIDI 43), with chromatic approaches
# Bar 2: D2 -> Eb2 -> G2 -> A2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0), # F#4
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=3.0), # A4
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=3.0)  # C#5
]
piano.notes.extend(piano_notes)

# Sax: Motif - D4 (62), F#4 (67), Bb4 (71), resolve on D5 (67)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Full ensemble (3.0 - 4.5s)

# Bass: Bb2 (MIDI 46), D2 (MIDI 38), with chromatic approaches
# Bar 3: Bb2 -> B2 -> D2 -> Eb2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.0)
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G-Bb-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5), # Bb4
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=4.5), # D5
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=4.5)  # F5
]
piano.notes.extend(piano_notes)

# Sax: Motif variation - G4 (67), Bb4 (71), D5 (74), resolve on G5 (79)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=74, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=79, start=3.75, end=4.0)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
# Hi-hat on every eighth
for i in range(0, 3):
    start = 3.0 + i * 0.375
    end = start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 4: Full ensemble (4.5 - 6.0s)

# Bass: A2 (MIDI 45), C2 (MIDI 40), with chromatic approaches
# Bar 4: A2 -> Bb2 -> C2 -> D2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=46, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=40, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.5)
]
bass.notes.extend(bass_notes)

# Piano: Cmaj7 (C-E-G-B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0), # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0), # E4
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=6.0), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0)  # B4
]
piano.notes.extend(piano_notes)

# Sax: Motif variation - C4 (60), E4 (64), G4 (67), resolve on C5 (68)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.5)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5))
# Hi-hat on every eighth
for i in range(0, 2):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
