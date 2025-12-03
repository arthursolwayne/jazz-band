
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI drum kits are on same program
sax_program = pretty_midi.instrument_name_to_program('Alto Sax')

# Add instruments to the MIDI file
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Time settings (160 BPM, 4/4)
bpm = 160
ticks_per_beat = pm.time_signature_changes[0].denominator * 4  # 4/4 time
tick_per_second = (bpm / 60) * ticks_per_beat
duration_seconds = 6.0  # 4 bars
total_ticks = int(duration_seconds * tick_per_second)

# Create a function to convert time to ticks
def time_to_ticks(time):
    return int(time * tick_per_second)

# Bars and their timings
bar_length = time_to_ticks(1.5)  # 1.5 seconds per bar

# -- DRUMS (Little Ray) --
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Set up hihat
hihat_note = 42  # MIDI note for hihat
hihat_velocity = 70
for tick in range(0, total_ticks, time_to_ticks(0.125)):  # every eighth note
    note = pretty_midi.Note(velocity=hihat_velocity, pitch=hihat_note, start=tick, end=tick + time_to_ticks(0.125))
    drums.notes.append(note)

# Set up kick (beat 1 and 3)
kick_note = 36  # MIDI note for kick
for bar in range(4):
    kick_start = bar * bar_length
    note = pretty_midi.Note(velocity=100, pitch=kick_note, start=kick_start, end=kick_start + time_to_ticks(0.125))
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=kick_note, start=kick_start + time_to_ticks(0.5), end=kick_start + time_to_ticks(0.625))
    drums.notes.append(note)

# Set up snare (beat 2 and 4)
snare_note = 38  # MIDI note for snare
for bar in range(4):
    snare_start = bar * bar_length + time_to_ticks(0.25)
    note = pretty_midi.Note(velocity=90, pitch=snare_note, start=snare_start, end=snare_start + time_to_ticks(0.125))
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=snare_note, start=snare_start + time_to_ticks(0.75), end=snare_start + time_to_ticks(0.875))
    drums.notes.append(note)

# -- BASS (Marcus) --
# Walking line with roots and fifths, chromatic approaches. In F minor (Fm7).

# Bar 1: F - Gb - G - Ab (root, chromatic down, root, chromatic down)
# Bar 2: Bb - A - G - Ab (fifth, chromatic up, root, chromatic down)
# Bar 3: F - Gb - G - Ab (root, chromatic down, root, chromatic down)
# Bar 4: Bb - A - G - F (fifth, chromatic up, root, root)

root_f = 65  # F3
fifth_b = 69  # Bb3
chromatic_down = [64, 65]  # Gb3 (64), F3 (65)
chromatic_up = [65, 66]    # F3 (65), G3 (66)

# Bar 1
for i, note in enumerate(chromatic_down + chromatic_down):
    start = i * time_to_ticks(0.25)
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + time_to_ticks(0.25))
    bass.notes.append(note_obj)

# Bar 2
for i, note in enumerate([fifth_b] + chromatic_up + [root_f]):
    start = i * time_to_ticks(0.25) + bar_length
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + time_to_ticks(0.25))
    bass.notes.append(note_obj)

# Bar 3
for i, note in enumerate(chromatic_down + chromatic_down):
    start = i * time_to_ticks(0.25) + 2 * bar_length
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + time_to_ticks(0.25))
    bass.notes.append(note_obj)

# Bar 4
for i, note in enumerate([fifth_b] + chromatic_up + [root_f]):
    start = i * time_to_ticks(0.25) + 3 * bar_length
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + time_to_ticks(0.25))
    bass.notes.append(note_obj)

# -- PIANO (Diane) --
# Open voicings, different chord each bar, resolve on the last
# Bar 1: Fm7 (F, Ab, C, Eb)
# Bar 2: Bb7 (Bb, D, F, Ab)
# Bar 3: Fm7 (F, Ab, C, Eb)
# Bar 4: Bb7 (Bb, D, F, Ab)

# Fm7 (F, Ab, C, Eb)
chord1 = [65, 68, 69, 62]
# Bb7 (Bb, D, F, Ab)
chord2 = [69, 67, 65, 68]
# Fm7 again
chord3 = [65, 68, 69, 62]
# Bb7 again
chord4 = [69, 67, 65, 68]

# Bar 1
for note in chord1:
    start = time_to_ticks(0.0)  # start on beat 1
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + time_to_ticks(0.5))  # hold for half bar
    piano.notes.append(note_obj)

# Bar 2
for note in chord2:
    start = bar_length  # start on beat 2
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + time_to_ticks(0.5))
    piano.notes.append(note_obj)

# Bar 3
for note in chord3:
    start = 2 * bar_length  # start on beat 3
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + time_to_ticks(0.5))
    piano.notes.append(note_obj)

# Bar 4
for note in chord4:
    start = 3 * bar_length  # start on beat 4
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + time_to_ticks(0.5))
    piano.notes.append(note_obj)

# -- SAX (Dante) -- 
# Short motif: Start with a phrase, leave it hanging, return and finish it.
# Motif in F minor: F, Gb, G, Ab (same as bass line but with a slight twist)

# Bar 1: F (65), Gb (64) — two notes, leave it hanging
note1 = pretty_midi.Note(velocity=100, pitch=65, start=0, end=0.75)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=0.75, end=1.5)
sax.notes.append(note1)
sax.notes.append(note2)

# Bar 2: Hold the Gb, then resolve to F
note3 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25)
note4 = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0)
sax.notes.append(note3)
sax.notes.append(note4)

# Bar 3: Repeat the motif, but slightly higher in texture
note5 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75)
note6 = pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5)
sax.notes.append(note5)
sax.notes.append(note6)

# Bar 4: Resolve the tension — G (67) to F (65), with a slight delay
note7 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25)
note8 = pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=6.0)
sax.notes.append(note7)
sax.notes.append(note8)

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
