
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with time signature 4/4 and tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
track_drums = pretty_midi.Instrument(program=10)  # Drums
track_bass = pretty_midi.Instrument(program=33)   # Bass
track_piano = pretty_midi.Instrument(program=0)   # Piano
track_sax = pretty_midi.Instrument(program=64)    # Tenor Sax

# Key is F major
key = 'F'

# Time per bar: 1.5 seconds (160 BPM => 60/160 * 4 = 1.5)
time_per_bar = 1.5
time_per_beat = time_per_bar / 4  # 0.375 seconds per beat

# Bar 1: Drums only — kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0 to 1.5 seconds)
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3 (beats 0 and 2)
kick_times = [bar1_start, bar1_start + 2 * time_per_beat]
for time in kick_times:
    note = pretty_midi.Note(
        velocity=90,
        pitch=36,  # Kick drum
        start=time,
        end=time + 0.1
    )
    track_drums.notes.append(note)

# Snare on 2 and 4 (beats 1 and 3)
snare_times = [bar1_start + time_per_beat, bar1_start + 3 * time_per_beat]
for time in snare_times:
    note = pretty_midi.Note(
        velocity=90,
        pitch=38,  # Snare drum
        start=time,
        end=time + 0.1
    )
    track_drums.notes.append(note)

# Hi-hat on every eighth note
for i in range(0, 8):
    time = bar1_start + i * time_per_beat / 2
    note = pretty_midi.Note(
        velocity=80,
        pitch=42,  # Hi-hat
        start=time,
        end=time + 0.05
    )
    track_drums.notes.append(note)

# Bar 2: Everyone comes in
bar2_start = bar1_end

# Saxophone melody — short motif, starts on F (72), then D (62), then A (69), then F (72) — leave it hanging
sax_note1 = pretty_midi.Note(
    velocity=100,
    pitch=72,  # F
    start=bar2_start,
    end=bar2_start + 0.375
)
track_sax.notes.append(sax_note1)

sax_note2 = pretty_midi.Note(
    velocity=100,
    pitch=62,  # D
    start=bar2_start + 0.375,
    end=bar2_start + 0.75
)
track_sax.notes.append(sax_note2)

sax_note3 = pretty_midi.Note(
    velocity=100,
    pitch=69,  # A
    start=bar2_start + 0.75,
    end=bar2_start + 1.125
)
track_sax.notes.append(sax_note3)

# Bar 3: Bass walks, chromatic line
# F (72), G (71), Ab (70), A (69), Bb (67), B (69), C (72), D (74)
# Slight chromatic deviation, not a pattern

bass_notes = [
    (72, bar2_start + 0.0, bar2_start + 0.375),    # F
    (71, bar2_start + 0.375, bar2_start + 0.75),    # G
    (70, bar2_start + 0.75, bar2_start + 1.125),    # Ab
    (69, bar2_start + 1.125, bar2_start + 1.5),     # A
    (67, bar2_start + 1.5, bar2_start + 1.875),     # Bb
    (69, bar2_start + 1.875, bar2_start + 2.25),     # B
    (72, bar2_start + 2.25, bar2_start + 2.625),     # C
    (74, bar2_start + 2.625, bar2_start + 3.0),      # D
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=start,
        end=end
    )
    track_bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2: Chord on 2 (beat 1), F7 (F A C Eb)
# Bar 3: Chord on 4 (beat 3), Dm7 (D F A C)
# Bar 4: Chord on 2 (beat 1), G7 (G B D F)
# Bar 4: Chord on 4 (beat 3), Cmaj7 (C E G B)

# Bar 2: F7 on beat 1 (0.375s)
chord_notes_F7 = [72, 76, 79, 74]  # F, A, C, Eb
for pitch in chord_notes_F7:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=bar2_start + 0.375,
        end=bar2_start + 0.75
    )
    track_piano.notes.append(note)

# Bar 3: Dm7 on beat 3 (1.125s)
chord_notes_Dm7 = [62, 67, 72, 76]  # D, F, A, C
for pitch in chord_notes_Dm7:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=bar2_start + 1.125,
        end=bar2_start + 1.5
    )
    track_piano.notes.append(note)

# Bar 4: G7 on beat 1 (1.875s)
chord_notes_G7 = [71, 76, 79, 74]  # G, B, D, F
for pitch in chord_notes_G7:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=bar2_start + 1.875,
        end=bar2_start + 2.25
    )
    track_piano.notes.append(note)

# Bar 4: Cmaj7 on beat 3 (2.625s)
chord_notes_Cmaj7 = [60, 64, 67, 72]  # C, E, G, B
for pitch in chord_notes_Cmaj7:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=bar2_start + 2.625,
        end=bar2_start + 3.0
    )
    track_piano.notes.append(note)

# Add instruments to the MIDI file
midi.instruments = [track_drums, track_bass, track_piano, track_sax]

# Save the MIDI file
midi.write("dante_intro.mid")
