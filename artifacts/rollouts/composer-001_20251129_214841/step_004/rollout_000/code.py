
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds per bar at 120 BPM
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3 (beats 0 and 2)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4 (beats 1 and 3)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Start with sax melody
bar_start = 1.5
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start, end=bar_start + 0.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 0.75, end=bar_start + 1.5),  # E4
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=bar_start, end=bar_start + 0.375),  # C3
    pretty_midi.Note(velocity=80, pitch=41, start=bar_start + 0.375, end=bar_start + 0.75),  # C#3
    pretty_midi.Note(velocity=80, pitch=43, start=bar_start + 0.75, end=bar_start + 1.125),  # D#3
    pretty_midi.Note(velocity=80, pitch=44, start=bar_start + 1.125, end=bar_start + 1.5),  # E3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 (C E G B)
    pretty_midi.Note(velocity=80, pitch=60, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=64, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=67, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=71, start=bar_start + 0.375, end=bar_start + 0.75),
    # Bar 3: F7 (F A C E)
    pretty_midi.Note(velocity=80, pitch=65, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=69, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=72, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=76, start=bar_start + 2.25, end=bar_start + 2.625),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar_start + (bar - 2) * bar_length
    # Kick on 1 and 3 (beats 0 and 2)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4 (beats 1 and 3)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bar 3: Continue sax melody
bar_start = 3.0
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start, end=bar_start + 0.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 0.75, end=bar_start + 1.5),  # A4
]
sax.notes.extend(sax_notes)

# Bar 4: End with a resolution
bar_start = 4.5
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start, end=bar_start + 0.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 0.75, end=bar_start + 1.5),  # E4
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=bar_start, end=bar_start + 0.375),  # F3
    pretty_midi.Note(velocity=80, pitch=46, start=bar_start + 0.375, end=bar_start + 0.75),  # F#3
    pretty_midi.Note(velocity=80, pitch=48, start=bar_start + 0.75, end=bar_start + 1.125),  # G#3
    pretty_midi.Note(velocity=80, pitch=49, start=bar_start + 1.125, end=bar_start + 1.5),  # A3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: G7 (G B D F)
    pretty_midi.Note(velocity=80, pitch=67, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=71, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=74, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=78, start=bar_start + 0.375, end=bar_start + 0.75),
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
