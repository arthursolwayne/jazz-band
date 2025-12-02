
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
pm.tempo = 160

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Drums use same program
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the PrettyMIDI object
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Time per bar (160 BPM, 4/4 time)
time_per_bar = 60.0 / 160 * 4  # in seconds
bar_duration = time_per_bar

# Define the key: D major
key = 'D'

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

#------------------------------------------------------------
# 1. Bar 1: Little Ray (Drums) - Set it up, make them wait
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Make the groove feel alive, avoid predictable patterns

# Define the beat (in seconds)
beat = 60.0 / 160  # 0.375 seconds per beat

# Hit on 1 and 3: kick
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0, end=beat)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=2*beat, end=3*beat)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=beat, end=2*beat)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=3*beat, end=4*beat)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=i * (beat / 2), end=(i + 1) * (beat / 2))
    drums.notes.append(hihat)

#------------------------------------------------------------
# 2. Bar 2: Everyone comes in
# Sax: Start the motif — a short, singing phrase
# D is the root, so we'll use notes in the D major scale: D, E, F#, G, A, B, C#

# Motif (D, E, F#, G) in 8th notes, starting at time=bar_duration
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar_duration, end=bar_duration + beat / 2),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=bar_duration + beat / 2, end=bar_duration + beat),  # E5
    pretty_midi.Note(velocity=100, pitch=66, start=bar_duration + beat, end=bar_duration + 3 * beat / 2),  # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=bar_duration + 3 * beat / 2, end=bar_duration + 2 * beat),  # G5
    pretty_midi.Note(velocity=100, pitch=62, start=bar_duration + 2 * beat, end=bar_duration + 2.5 * beat),  # D5 (half note)
]

sax.notes.extend(sax_notes)

#------------------------------------------------------------
# 3. Bar 2: Bass (Marcus) — Walking line, chromatic approaches
# D -> C# -> D -> E, etc.

# Walking bass pattern (D, C#, D, E) in 16th notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar_duration, end=bar_duration + beat / 4),  # D3
    pretty_midi.Note(velocity=80, pitch=61, start=bar_duration + beat / 4, end=bar_duration + beat / 2),  # C#3
    pretty_midi.Note(velocity=80, pitch=62, start=bar_duration + beat / 2, end=bar_duration + 3 * beat / 4),  # D3
    pretty_midi.Note(velocity=80, pitch=64, start=bar_duration + 3 * beat / 4, end=bar_duration + beat),  # E3
    pretty_midi.Note(velocity=80, pitch=62, start=bar_duration + beat, end=bar_duration + 5 * beat / 4),  # D3
    pretty_midi.Note(velocity=80, pitch=61, start=bar_duration + 5 * beat / 4, end=bar_duration + 3 * beat / 2),  # C#3
    pretty_midi.Note(velocity=80, pitch=62, start=bar_duration + 3 * beat / 2, end=bar_duration + 7 * beat / 4),  # D3
    pretty_midi.Note(velocity=80, pitch=64, start=bar_duration + 7 * beat / 4, end=bar_duration + 2 * beat),  # E3
]

bass.notes.extend(bass_notes)

#------------------------------------------------------------
# 4. Bar 2: Piano (Diane) — 7th chords on 2 and 4, comp on 2 and 4, keep it moving
# D7 on 2 and 4
piano_notes = []

# D7 chord: D (62), F# (66), A (69), C (60)
# 7th chord: 62, 66, 69, 60

# Comp on 2 and 4 (times 1.5 and 2.0 seconds)
# Use 6th and 9th intervals to color the space
for t in [bar_duration + beat / 2, bar_duration + beat]:
    # 6th (B) and 9th (F#)
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=t, end=t + beat / 4))  # A (69)
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=t, end=t + beat / 4))  # F# (66)
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=t, end=t + beat / 4))  # D (62)

piano.notes.extend(piano_notes)

#------------------------------------------------------------
# 5. Bar 3: Sax — Continue the motif, leave it hanging
# You start the motif again, but this time let it hang on the last note

# D5 (62) again, but this time as a quarter note
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=bar_duration * 2, end=bar_duration * 2 + beat)
sax.notes.append(sax_note)

#------------------------------------------------------------
# 6. Bar 3: Bass (Marcus) — Keep walking
# D -> C# -> D -> E -> F# -> G -> A -> B, etc.
# But don't repeat the same pattern

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=bar_duration * 2, end=bar_duration * 2 + beat / 4),  # E3
    pretty_midi.Note(velocity=80, pitch=66, start=bar_duration * 2 + beat / 4, end=bar_duration * 2 + beat / 2),  # F#3
    pretty_midi.Note(velocity=80, pitch=67, start=bar_duration * 2 + beat / 2, end=bar_duration * 2 + 3 * beat / 4),  # G3
    pretty_midi.Note(velocity=80, pitch=69, start=bar_duration * 2 + 3 * beat / 4, end=bar_duration * 2 + beat),  # A3
    pretty_midi.Note(velocity=80, pitch=64, start=bar_duration * 2 + beat, end=bar_duration * 2 + 5 * beat / 4),  # E3
    pretty_midi.Note(velocity=80, pitch=66, start=bar_duration * 2 + 5 * beat / 4, end=bar_duration * 2 + 3 * beat / 2),  # F#3
    pretty_midi.Note(velocity=80, pitch=67, start=bar_duration * 2 + 3 * beat / 2, end=bar_duration * 2 + 7 * beat / 4),  # G3
    pretty_midi.Note(velocity=80, pitch=69, start=bar_duration * 2 + 7 * beat / 4, end=bar_duration * 2 + 2 * beat),  # A3
]

bass.notes.extend(bass_notes)

#------------------------------------------------------------
# 7. Bar 3: Piano (Diane) — Keep the color, comp on 2 and 4
# Use extended harmony (9th, 11th) to keep it moving

piano_notes = []

for t in [bar_duration * 2 + beat / 2, bar_duration * 2 + beat]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=t, end=t + beat / 4))  # B (71)
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=t, end=t + beat / 4))  # F# (66)
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=t, end=t + beat / 4))  # D (62)

piano.notes.extend(piano_notes)

#------------------------------------------------------------
# 8. Bar 4: Sax — Come back and finish the motif
# End on a resolution, but keep it open-ended

# Now we finish the motif with a G5 (67), ending on the downbeat of bar 4
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=bar_duration * 3, end=bar_duration * 3 + beat)
sax.notes.append(sax_note)

#------------------------------------------------------------
# 9. Bar 4: Bass — Resolve the walking line to A or G

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=bar_duration * 3, end=bar_duration * 3 + beat / 4),  # A3
    pretty_midi.Note(velocity=80, pitch=67, start=bar_duration * 3 + beat / 4, end=bar_duration * 3 + beat / 2),  # G3
    pretty_midi.Note(velocity=80, pitch=69, start=bar_duration * 3 + beat / 2, end=bar_duration * 3 + 3 * beat / 4),  # A3
    pretty_midi.Note(velocity=80, pitch=67, start=bar_duration * 3 + 3 * beat / 4, end=bar_duration * 3 + beat),  # G3
]

bass.notes.extend(bass_notes)

#------------------------------------------------------------
# 10. Bar 4: Piano — Close the space, but don't resolve

piano_notes = []

for t in [bar_duration * 3 + beat / 2, bar_duration * 3 + beat]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=t, end=t + beat / 4))  # A (69)
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=t, end=t + beat / 4))  # F# (66)
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=t, end=t + beat / 4))  # D (62)

piano.notes.extend(piano_notes)

#------------------------------------------------------------
# 11. Bar 4: Drums — Keep the energy, but don't fully resolve

# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_duration * 3, end=bar_duration * 3 + beat)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_duration * 3 + 2 * beat, end=bar_duration * 3 + 3 * beat)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_duration * 3 + beat, end=bar_duration * 3 + 2 * beat)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_duration * 3 + 3 * beat, end=bar_duration * 3 + 4 * beat)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar_duration * 3 + i * (beat / 2), end=bar_duration * 3 + (i + 1) * (beat / 2))
    drums.notes.append(hihat)

# Write the MIDI file
pm.write("dante_intro.mid")

print("MIDI file 'dante_intro.mid' has been created.")
