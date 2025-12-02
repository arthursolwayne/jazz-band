
import pretty_midi

# Define parameters
tempo = 160  # BPM
time_signature = (4, 4)
key = 'Dm'  # D minor
duration = 6.0  # 4 bars at 160 BPM

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Time per bar (in seconds)
bar_duration = 60.0 / tempo * 4  # 6 seconds for 4 bars

# Define instrument programs
program_tenor_sax = 67  # Tenor sax
program_bass = 33  # Double Bass
program_piano = 0  # Acoustic Piano
program_drums = 0  # Drums

# Add instruments
instrument_tenor = pretty_midi.Instrument(program=program_tenor_sax)
instrument_bass = pretty_midi.Instrument(program=program_bass)
instrument_piano = pretty_midi.Instrument(program=program_piano)
instrument_drums = pretty_midi.Instrument(program=program_drums)

pm.instruments.append(instrument_tenor)
pm.instruments.append(instrument_bass)
pm.instruments.append(instrument_piano)
pm.instruments.append(instrument_drums)

# Define note durations in seconds
note_duration = 0.375  # 1 beat at 160 BPM

# DRUMS: Little Ray
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0.0 - 1.5s)
instrument_drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
instrument_drums.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=0.75, end=1.125))  # Kick on 3
instrument_drums.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=0.375, end=0.75))  # Snare on 2
instrument_drums.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.125, end=1.5))  # Snare on 4
instrument_drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5))  # Hihat on every eighth

# BASS: Marcus
# Walking line, chromatic approaches, never the same note twice

# Bar 1: Dm (D F A C) -> Dm7 (D F A C) -> walking line starting from D
# Bar 1: D -> Eb -> F -> G -> A (chromatic approach)
note_times = [0.0, 0.375, 0.75, 1.125, 1.5]
notes = [62, 63, 64, 65, 67]  # D, Eb, F, G, A

for t, n in zip(note_times, notes):
    instrument_bass.notes.append(pretty_midi.Note(velocity=80, pitch=n, start=t, end=t + 0.375))

# PIANO: Diane
# Comp on 2 and 4, 7th chords, Dm7

# Bar 1: Dm7 (D F A C) on beat 2 and 4
instrument_piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=0.375, end=0.75))  # D
instrument_piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=0.375, end=0.75))  # F
instrument_piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=0.375, end=0.75))  # A
instrument_piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=0.375, end=0.75))  # C

instrument_piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.125, end=1.5))  # D
instrument_piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.125, end=1.5))  # F
instrument_piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.125, end=1.5))  # A
instrument_piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.125, end=1.5))  # C

# TENOR SAX: You
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: D to F to Bb to D — but phrased with a rest and delay

# Bar 1: Rest (0.0 - 1.5s) — let the drums and bass set the scene

# Bar 2: Start motive
# D (62) — quarter note
# F (64) — eighth note, then rest
# Bb (60) — eighth note, then rest
# D (62) — quarter note on beat 3

note_times_tenor = [1.5, 1.875, 2.25, 2.625]
notes_tenor = [62, 64, 60, 62]

for t, n in zip(note_times_tenor, notes_tenor):
    instrument_tenor.notes.append(pretty_midi.Note(velocity=100, pitch=n, start=t, end=t + 0.375))

# Write the MIDI file
pm.write('dante_intro.mid')
print("MIDI file 'dante_intro.mid' has been created.")
