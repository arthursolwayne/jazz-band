
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instrument tracks
sax_program = pretty_midi.programs.Program(64)  # Tenor Saxophone
bass_program = pretty_midi.programs.Program(33)  # Electric Bass
piano_program = pretty_midi.programs.Program(0)  # Acoustic Piano
drum_program = pretty_midi.programs.Program(9)  # Acoustic Drums

sax_track = pretty_midi.Instrument(program=sax_program)
bass_track = pretty_midi.Instrument(program=bass_program)
piano_track = pretty_midi.Instrument(program=piano_program)
drum_track = pretty_midi.Instrument(program=drum_program)

# Add all tracks to the MIDI file
midi.instruments.append(sax_track)
midi.instruments.append(bass_track)
midi.instruments.append(piano_track)
midi.instruments.append(drum_track)

# Set time signature and tempo
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempos = [pretty_midi.TempoChange(160, 0)]

# Convert BPM to seconds per beat
beats_per_second = 160 / 60
beat_duration = 1 / beats_per_second  # 0.375 seconds per beat
bar_duration = 4 * beat_duration  # 1.5 seconds per bar

# --- BARS 1 to 4 ---
# Bar 1 (Little Ray alone)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
bar1_start = 0
drum_notes = [
    (1, bar1_start + 0),       # Kick on 1
    (2, bar1_start + 0.5),     # Hihat on 1 & 1/2
    (1, bar1_start + 1),       # Kick on 2
    (2, bar1_start + 1.5),     # Hihat on 2 & 1/2
    (3, bar1_start + 1.5),     # Snare on 2
    (1, bar1_start + 2),       # Kick on 3
    (2, bar1_start + 2.5),     # Hihat on 3 & 1/2
    (1, bar1_start + 3),       # Kick on 4
    (2, bar1_start + 3.5),     # Hihat on 4 & 1/2
    (3, bar1_start + 3.5),     # Snare on 4
]

for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1)
    drum_track.notes.append(note)

# Bar 2: Everyone in. You take the melody. Short motif with rests.
bar2_start = bar_duration

# Saxophone motif in Fm (F, Ab, Bb, D)
# Notes: F (65), Ab (67), Bb (69), D (70)
# Time: Bar 2, beat 1 (0.375s), rest for 0.125s, then note for 0.25s
# Then rest for 0.125s, then note for 0.25s
# Then rest for 0.125s, then note for 0.25s
# Then rest for 0.125s, then note for 0.25s

sax_notes = [
    (65, bar2_start + 0.375, 0.25),  # F on beat 1
    (67, bar2_start + 0.75, 0.25),   # Ab on beat 2
    (69, bar2_start + 1.125, 0.25),  # Bb on beat 3
    (70, bar2_start + 1.5, 0.25),    # D on beat 4
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax_track.notes.append(note)

# Bass line: walking line with chromatic approaches
# Start on E (60) and walk down, with chromatic approaches (61 -> 60 instead of 59)
bass_notes = [
    (60, bar2_start + 0, 0.375),  # E on beat 1
    (61, bar2_start + 0.375, 0.375),  # F on beat 2
    (60, bar2_start + 0.75, 0.375),  # E on beat 3
    (58, bar2_start + 1.125, 0.375),  # D on beat 4
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    bass_track.notes.append(note)

# Piano: 7th chords on beats 2 and 4
# Fm7 = F, Ab, C, Eb (65, 67, 72, 69)
# Root position on beat 2 and 4

piano_notes = [
    (65, bar2_start + 0.75, 0.375), # F
    (67, bar2_start + 0.75, 0.375), # Ab
    (69, bar2_start + 0.75, 0.375), # Eb
    (72, bar2_start + 0.75, 0.375), # C
    (65, bar2_start + 1.5, 0.375),  # F
    (67, bar2_start + 1.5, 0.375),  # Ab
    (69, bar2_start + 1.5, 0.375),  # Eb
    (72, bar2_start + 1.5, 0.375),  # C
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    piano_track.notes.append(note)

# Bar 3 and 4: Same rhythm, same feels
# Drums repeat the same pattern
bar3_start = 2 * bar_duration
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=bar3_start + time, end=bar3_start + time + 0.1)
    drum_track.notes.append(note)

bar4_start = 3 * bar_duration
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=bar4_start + time, end=bar4_start + time + 0.1)
    drum_track.notes.append(note)

# --- Output MIDI file ---
midi.write("dantes_intro.mid")

print("MIDI file generated: dantes_intro.mid")
