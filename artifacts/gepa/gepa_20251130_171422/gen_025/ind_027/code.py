
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
tenor_sax = Instrument(program=Program.TENOR_SAXOPHONE)
bass = Instrument(program=Program.BASS)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
drums = Instrument(program=Program.DRUMS)

# Add instruments to the PrettyMIDI object
pm.instruments.append(tenor_sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Time parameters
bpm = 160
beat = 60.0 / bpm
bar = beat * 4  # 6.0 seconds for 4 bars
note_length = beat * 0.5  # Half note length for sax motif

# Bar 1: Drums only (setup)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1 = 0.0

# Kick on 1 and 3
drum_kick_1 = Note(36, bar_1, note_length, instrument=drums)
drum_kick_3 = Note(36, bar_1 + beat * 2, note_length, instrument=drums)
drums.notes.append(drum_kick_1)
drums.notes.append(drum_kick_3)

# Snare on 2 and 4
drum_snare_2 = Note(38, bar_1 + beat * 1, note_length, instrument=drums)
drum_snare_4 = Note(38, bar_1 + beat * 3, note_length, instrument=drums)
drums.notes.append(drum_snare_2)
drums.notes.append(drum_snare_4)

# Hihat on every eighth
hihat_notes = [bar_1 + beat * i * 0.5 for i in range(8)]
for note_time in hihat_notes:
    hihat = Note(42, note_time, beat * 0.25, instrument=drums)
    drums.notes.append(hihat)

# Bar 2: Everyone in

# Tenor sax motif (start and leave it hanging)
# Dm7: D, F, A, C
# Motif: D - F# - C - B (ascending with tension)
bar_2 = bar_1 + bar
note_times = [bar_2, bar_2 + beat * 0.5, bar_2 + beat * 1.5, bar_2 + beat * 2.0]

# D (62), F# (65), C (60), B (61)
note_heights = [62, 65, 60, 61]
note_velocities = [90, 85, 80, 95]  # Dynamic shading
for time, pitch, vel in zip(note_times, note_heights, note_velocities):
    note = Note(pitch, time, note_length, velocity=vel, instrument=tenor_sax)
    tenor_sax.notes.append(note)

# Bass line: Chromatic walking, active and melodic
# Dm7: D, F, A, C
# Bass line: D - F - E - D - C - D - F - E
bass_notes = [62, 65, 64, 62, 60, 62, 65, 64]
bass_times = [bar_2 + beat * i * 0.25 for i in range(8)]
bass_velocities = [75, 75, 70, 65, 65, 70, 75, 75]
for time, pitch, vel in zip(bass_times, bass_notes, bass_velocities):
    note = Note(pitch, time, beat * 0.25, velocity=vel, instrument=bass)
    bass.notes.append(note)

# Piano comp: 7th chords on 2 and 4, with emotion
# Dm7: D, F, A, C
# Bar 2: Comp on 2 and 4
chord_2 = [62, 65, 67, 69]  # D7 (with 9th or passing tone)
chord_4 = [62, 65, 67, 69]  # Same chord, but with subtle variation

# Note durations: 1/2 note on 2 and 4
piano_time_2 = bar_2 + beat * 1
piano_time_4 = bar_2 + beat * 3

# Spread and add dynamics
def comp_chord(pitch_list, time, vel_start, vel_end):
    for i, pitch in enumerate(pitch_list):
        duration = beat * 1.0
        velocity = vel_start + (vel_end - vel_start) * (i / len(pitch_list))
        note = Note(pitch, time, duration, velocity=velocity, instrument=piano)
        piano.notes.append(note)

comp_chord(chord_2, piano_time_2, 80, 90)
comp_chord(chord_4, piano_time_4, 85, 95)

# Bar 3: Continue with the motif, but return to finish it
bar_3 = bar_2 + bar

# Tenor sax motif: return and finish the line
note_times = [bar_3 + beat * 1.5, bar_3 + beat * 2.0, bar_3 + beat * 2.5]
# Complete the motif: B - D - F# (resolution)
note_heights = [61, 62, 65]
note_velocities = [95, 90, 85]
for time, pitch, vel in zip(note_times, note_heights, note_velocities):
    note = Note(pitch, time, note_length, velocity=vel, instrument=tenor_sax)
    tenor_sax.notes.append(note)

# Bass line: Continue with walking line
bass_notes = [62, 65, 64, 62, 60, 62, 65, 64]
bass_times = [bar_3 + beat * i * 0.25 for i in range(8)]
bass_velocities = [75, 75, 70, 65, 65, 70, 75, 75]
for time, pitch, vel in zip(bass_times, bass_notes, bass_velocities):
    note = Note(pitch, time, beat * 0.25, velocity=vel, instrument=bass)
    bass.notes.append(note)

# Piano comp: 7th chords on 2 and 4 again, with variation in voicings
chord_2 = [62, 65, 67, 69]  # D7
chord_4 = [62, 65, 67, 69]  # Same chord, with brighter voicing

comp_chord(chord_2, piano_time_2 + bar, 80, 90)
comp_chord(chord_4, piano_time_4 + bar, 85, 95)

# Bar 4: End with resolution and release
bar_4 = bar_3 + bar

# Tenor sax: Resolution note on beat 3, then rest
note = Note(62, bar_4 + beat * 2.0, note_length, velocity=80, instrument=tenor_sax)
tenor_sax.notes.append(note)

# Bass line: Resolve on D
note = Note(62, bar_4 + beat * 3.5, note_length, velocity=65, instrument=bass)
bass.notes.append(note)

# Piano: 7th chord on beat 4
chord_4 = [62, 65, 67, 69]
comp_chord(chord_4, bar_4 + beat * 3.0, 85, 95)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Kick on 1 and 3
drum_kick_1 = Note(36, bar_4, note_length, instrument=drums)
drum_kick_3 = Note(36, bar_4 + beat * 2, note_length, instrument=drums)
drums.notes.append(drum_kick_1)
drums.notes.append(drum_kick_3)

# Snare on 2 and 4
drum_snare_2 = Note(38, bar_4 + beat * 1, note_length, instrument=drums)
drum_snare_4 = Note(38, bar_4 + beat * 3, note_length, instrument=drums)
drums.notes.append(drum_snare_2)
drums.notes.append(drum_snare_4)

# Hihat on every eighth
hihat_notes = [bar_4 + beat * i * 0.5 for i in range(8)]
for note_time in hihat_notes:
    hihat = Note(42, note_time, beat * 0.25, instrument=drums)
    drums.notes.append(hihat)

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file written as 'dante_intro.mid'")
