
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax_program = pretty_midi.programs.Program(64)  # Tenor Sax
bass_program = pretty_midi.programs.Program(33)  # Double Bass
piano_program = pretty_midi.programs.Program(0)  # Acoustic Piano
drums_program = pretty_midi.programs.Program(9)  # Acoustic Drums

sax_instrument = pretty_midi.Instrument(program=sax_program)
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
drum_instrument = pretty_midi.Instrument(program=drums_program)

pm.instruments.append(sax_instrument)
pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drum_instrument)

# Time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Calculate beat duration (0.375 seconds per beat)
beat_duration = 0.375
bar_duration = 1.5

# Bar 1: Drums only, mysterious groove
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36]  # Kick drum
snare_notes = [38]  # Snare drum
hihat_notes = [42]  # Hihat

# Kick on 1 and 3
kick_times = [0.0, 0.75]
for t in kick_times:
    drum_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=t, end=t + 0.15))

# Snare on 2 and 4
snare_times = [0.375, 1.125]
for t in snare_times:
    drum_instrument.notes.append(pretty_midi.Note(velocity=85, pitch=38, start=t, end=t + 0.15))

# Hihat on every eighth
hihat_times = [0.0, 0.375, 0.75, 1.125]
for t in hihat_times:
    drum_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05))

# Bar 2: Bass enters with chromatic walking line
# Fm7 - Bb7 - Eb7 - Ab7
# Chromatic walking line in Fm
bass_notes = [53, 51, 49, 50, 52, 51, 49, 50]
bass_durations = [0.375] * 8
bass_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]

for note, time, duration in zip(bass_notes, bass_times, bass_durations):
    bass_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + duration))

# Bar 2-3: Piano enters with sparse comping on 2 and 4
# Fm7 chord (F, Ab, Bb, Db) on beat 2 and 4
piano_notes = [
    # Bar 2: on 2
    (53, 0.375, 0.15),  # F
    (60, 0.375, 0.15),  # Ab
    (62, 0.375, 0.15),  # Bb
    (58, 0.375, 0.15),  # Db
    # Bar 3: on 2
    (53, 1.875, 0.15),
    (60, 1.875, 0.15),
    (62, 1.875, 0.15),
    (58, 1.875, 0.15),
]

for note, time, duration in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

# Bar 2-4: Saxophone motif
# 4-note motif starting on beat 1 of bar 2
# F, Bb, Ab, F#
sax_notes = [53, 62, 60, 63]
sax_durations = [0.375, 0.375, 0.375, 0.375]
sax_times = [1.5, 1.875, 2.25, 2.625]

for note, time, duration in zip(sax_notes, sax_times, sax_durations):
    sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

# Add some subtle variations in dynamics and timing
# Saxophone first note with slight delay
sax_instrument.notes[0].start += 0.05
sax_instrument.notes[0].velocity = 95

# Piano note on bar 2, beat 2: slightly delayed and quieter
piano_instrument.notes[3].start += 0.02
piano_instrument.notes[3].velocity = 90

# Save the MIDI file
pm.write("fm_intro.mid")
