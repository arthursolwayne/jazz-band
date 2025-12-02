
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0)   # F2
]
bass.notes.extend(bass_notes)

# Diane on piano (open voicings, different chord each bar, comp on 2 and 4)
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.0),  # A5
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0),  # E6
]
# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.75),  # Ab4
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),   # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.5),   # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),   # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),   # Bb3
])
piano.notes.extend(piano_notes)

# Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
# Bar 2
for i in range(2):
    start = 1.5 + i * 1.5
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))  # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875))  # Snare on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))  # Kick on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0))  # Snare on 4
    # Hihat on every eighth
    for j in range(8):
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.1875))

drums.notes.extend(drum_notes)

# Dante on tenor sax (short motif, start it, leave it hanging, come back and finish it)
# F4 (65), G4 (67), A4 (69), Bb4 (71), D5 (72), F5 (77)
# Motif: F4 - G4 - A4 (bar 2)
# Rest on bar 3
# Finish on bar 4: Bb4 - D5 - F5
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=77, start=3.25, end=3.375)   # F5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
