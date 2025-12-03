
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# 160 BPM = 60 / 160 = 0.375 seconds per beat
# 4/4 time, so 4 beats per bar = 1.5 seconds total per bar

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
bar_1_end = 1.5

# Kick on 1 and 3 (beat 0 and 2)
kick1 = pretty_midi.Note(velocity=90, pitch=36, start=bar_1_start, end=bar_1_start + 0.1)
kick2 = pretty_midi.Note(velocity=90, pitch=36, start=bar_1_start + 0.75, end=bar_1_start + 0.85)

# Snare on 2 and 4 (beat 1 and 3)
snare1 = pretty_midi.Note(velocity=85, pitch=38, start=bar_1_start + 0.375, end=bar_1_start + 0.475)
snare2 = pretty_midi.Note(velocity=85, pitch=38, start=bar_1_start + 1.125, end=bar_1_start + 1.225)

# Hihat on every eighth (8 notes per bar)
hihat_notes = [
    pretty_midi.Note(velocity=70, pitch=42, start=bar_1_start + i * 0.375, end=bar_1_start + i * 0.375 + 0.1)
    for i in range(8)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 2: Full quartet enters (1.5 - 3.0s)

bar_2_start = 1.5
bar_2_end = 3.0

# Bass line: walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=bar_2_start, end=bar_2_start + 0.1),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=bar_2_start + 0.375, end=bar_2_start + 0.475),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=bar_2_start + 0.75, end=bar_2_start + 0.85),    # A2
    pretty_midi.Note(velocity=80, pitch=42, start=bar_2_start + 1.125, end=bar_2_start + 1.225),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=bar_2_start + 1.5, end=bar_2_start + 1.6),      # D2 (next bar)
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=bar_2_start, end=bar_2_start + 0.1),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=bar_2_start, end=bar_2_start + 0.1),  # F#4
    pretty_midi.Note(velocity=85, pitch=69, start=bar_2_start, end=bar_2_start + 0.1),  # A4
    pretty_midi.Note(velocity=85, pitch=71, start=bar_2_start, end=bar_2_start + 0.1),  # C#4

    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=85, pitch=67, start=bar_2_start + 1.5, end=bar_2_start + 1.6),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=bar_2_start + 1.5, end=bar_2_start + 1.6),  # B4
    pretty_midi.Note(velocity=85, pitch=69, start=bar_2_start + 1.5, end=bar_2_start + 1.6),  # D4
    pretty_midi.Note(velocity=85, pitch=64, start=bar_2_start + 1.5, end=bar_2_start + 1.6),  # F4

    # Bar 4: C7 (C E G B)
    pretty_midi.Note(velocity=85, pitch=60, start=bar_2_start + 3.0, end=bar_2_start + 3.1),  # C4
    pretty_midi.Note(velocity=85, pitch=64, start=bar_2_start + 3.0, end=bar_2_start + 3.1),  # E4
    pretty_midi.Note(velocity=85, pitch=67, start=bar_2_start + 3.0, end=bar_2_start + 3.1),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=bar_2_start + 3.0, end=bar_2_start + 3.1),  # B4
]

piano.notes.extend(piano_notes)

# Drums: continue the pattern for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(2, 5):
    bar_start = bar_1_end + (bar - 2) * 1.5
    kick1 = pretty_midi.Note(velocity=90, pitch=36, start=bar_start, end=bar_start + 0.1)
    kick2 = pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 0.75, end=bar_start + 0.85)
    snare1 = pretty_midi.Note(velocity=85, pitch=38, start=bar_start + 0.375, end=bar_start + 0.475)
    snare2 = pretty_midi.Note(velocity=85, pitch=38, start=bar_start + 1.125, end=bar_start + 1.225)
    hihat_notes = [
        pretty_midi.Note(velocity=70, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1)
        for i in range(8)
    ]
    drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Sax: Your solo motif (bar 2-4)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 - start of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=bar_2_start, end=bar_2_start + 0.1),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_2_start + 0.25, end=bar_2_start + 0.35),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_2_start + 0.5, end=bar_2_start + 0.6),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=bar_2_start + 0.75, end=bar_2_start + 0.85),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_2_start + 1.0, end=bar_2_start + 1.1),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_2_start + 1.25, end=bar_2_start + 1.35),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=bar_2_start + 1.5, end=bar_2_start + 1.6),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=bar_2_start + 1.75, end=bar_2_start + 1.85),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_2_start + 2.0, end=bar_2_start + 2.1),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_2_start + 2.25, end=bar_2_start + 2.35),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=bar_2_start + 2.5, end=bar_2_start + 2.6),  # D4
]

sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
