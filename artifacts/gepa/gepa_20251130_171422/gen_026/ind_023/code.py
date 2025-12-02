
import pretty_midi

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key signature to F major (no sharps or flats)
# In MIDI, key signatures are stored as a number of sharps/flats
# F major has 1 flat (Bb), so we use -1
midi.key_signature_changes = [pretty_midi.KeySignature(-1, 0)]

# Instrument tracks
saxophone_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')

saxophone = pretty_midi.Instrument(program=saxophone_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Add instruments to the MIDI file
midi.instruments = [saxophone, bass, piano, drums]

# Time per bar in seconds at 160 BPM (160 beats per minute = 0.375 seconds per beat)
time_per_beat = 0.375
time_per_bar = time_per_beat * 4  # 4 beats per bar

# Bar 1: Drums only - build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Use dynamic variation

# Kick on 1 and 3 (beats 0 and 2)
kick_notes = [36, 36]
kick_times = [0, 2]  # in beats

# Snare on 2 and 4 (beats 1 and 3)
snare_notes = [38, 38]
snare_times = [1, 3]

# Hihat on every eighth note (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5)
hihat_notes = [42] * 8
hihat_times = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]

# Add dynamic variation to the hihat
hihat_velocities = [64, 80, 64, 70, 64, 80, 64, 70]

# Create the hihat notes
for note, time, velocity in zip(hihat_notes, hihat_times, hihat_velocities):
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time * time_per_beat, end=(time + 0.125) * time_per_beat)
    drums.notes.append(note)

# Create the kick notes
for note, time in zip(kick_notes, kick_times):
    note = pretty_midi.Note(velocity=90, pitch=note, start=time * time_per_beat, end=(time + 0.125) * time_per_beat)
    drums.notes.append(note)

# Create the snare notes
for note, time in zip(snare_notes, snare_times):
    note = pretty_midi.Note(velocity=100, pitch=note, start=time * time_per_beat, end=(time + 0.125) * time_per_beat)
    drums.notes.append(note)

# Bar 2-4: Full ensemble

# --- Bass Line (Marcus): Walking line with chromatic approaches, active and melodic ---
# F major scale: F G A Bb C D E
# Chromatic approach to each chord
bass_notes = [
    65, 64, 66, 65,  # F -> Bb (chromatic approach)
    67, 66, 68, 67,  # G -> C (chromatic approach)
    69, 70, 68, 69,  # A -> D (chromatic approach)
    71, 70, 72, 71   # Bb -> E (chromatic approach)
]
bass_times = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75]
bass_velocities = [60, 64, 60, 64, 60, 64, 60, 64, 60, 64, 60, 64, 60, 64, 60, 64]

for note, time, velocity in zip(bass_notes, bass_times, bass_velocities):
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time * time_per_beat, end=(time + 0.25) * time_per_beat)
    bass.notes.append(note)

# --- Piano (Diane): 7th chords, comp on 2 and 4 ---
# Time 1.0 (beat 2) and 3.0 (beat 4) in bar 2 (which is bar 1.5 in the timeline)
piano_notes = [
    # F7 (F, A, C, E) at beat 1.0
    65, 68, 72, 74,
    # D7 (D, F#, A, C) at beat 3.0
    67, 71, 69, 72
]
piano_times = [1.0, 1.0, 1.0, 1.0, 3.0, 3.0, 3.0, 3.0]
piano_velocities = [80, 80, 80, 80, 80, 80, 80, 80]

for note, time, velocity in zip(piano_notes, piano_times, piano_velocities):
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time * time_per_beat, end=(time + 0.25) * time_per_beat)
    piano.notes.append(note)

# --- Saxophone (You): The motif — concise, memorable, emotional ---
# Motif: F, Bb, C, Eb (F7)
# Start on beat 1.0, phrase over 3 beats, leave it hanging on beat 4.0
sax_notes = [65, 64, 67, 66]  # F, Bb, C, Eb
sax_times = [1.0, 1.0, 1.5, 2.0]
sax_velocities = [100, 100, 95, 100]

for note, time, velocity in zip(sax_notes, sax_times, sax_velocities):
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time * time_per_beat, end=(time + 0.25) * time_per_beat)
    saxophone.notes.append(note)

# Save the MIDI file
midi.write('dante_russo_intro.mid')

print("MIDI file 'dante_russo_intro.mid' has been created.")
