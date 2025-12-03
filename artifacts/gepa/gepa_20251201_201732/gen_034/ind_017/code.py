
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# BPM: 160
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0.0)]

# Time per beat: 0.375 seconds (60 / 160)
time_per_beat = 0.375
time_per_bar = time_per_beat * 4  # 1.5 seconds per bar

# Bar 1: Drums only
# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.0 + time_per_beat)
drum_kick2 = pretty_midi.Note(velocity=80, pitch=36, start=0.0 + 2 * time_per_beat, end=0.0 + 2 * time_per_beat + time_per_beat)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=80, pitch=38, start=0.0 + time_per_beat, end=0.0 + time_per_beat + time_per_beat)
drum_snare2 = pretty_midi.Note(velocity=80, pitch=38, start=0.0 + 3 * time_per_beat, end=0.0 + 3 * time_per_beat + time_per_beat)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(8):
    start = i * (time_per_beat / 2)
    end = start + (time_per_beat / 2)
    note = pretty_midi.Note(velocity=70, pitch=42, start=start, end=end)
    drums.notes.append(note)

# Bar 2:
# Bass: D2 (MIDI 38) - walking line with chromatic approaches
# D2 -> Eb2 -> D2 -> C2 -> D2 -> Eb2 -> D2 -> C2
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.5 + time_per_beat),
    pretty_midi.Note(velocity=90, pitch=39, start=1.5 + time_per_beat, end=1.5 + 2 * time_per_beat),
    pretty_midi.Note(velocity=90, pitch=38, start=1.5 + 2 * time_per_beat, end=1.5 + 3 * time_per_beat),
    pretty_midi.Note(velocity=90, pitch=36, start=1.5 + 3 * time_per_beat, end=1.5 + 4 * time_per_beat)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, each bar has a different chord, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.5 + time_per_beat),  # D (MIDI 62)
    pretty_midi.Note(velocity=85, pitch=65, start=1.5, end=1.5 + time_per_beat),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.5 + time_per_beat),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.5 + time_per_beat),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.0 + time_per_beat),  # C
    pretty_midi.Note(velocity=85, pitch=63, start=3.0, end=3.0 + time_per_beat),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.0 + time_per_beat),  # G
    pretty_midi.Note(velocity=85, pitch=70, start=3.0, end=3.0 + time_per_beat),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 4: Bb7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=59, start=4.5, end=4.5 + time_per_beat),  # Bb
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.5 + time_per_beat),  # D
    pretty_midi.Note(velocity=85, pitch=65, start=4.5, end=4.5 + time_per_beat),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.5 + time_per_beat),  # A
]
piano.notes.extend(piano_notes)

# Bar 2: Drums
# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.5 + time_per_beat)
drum_kick2 = pretty_midi.Note(velocity=80, pitch=36, start=1.5 + 2 * time_per_beat, end=1.5 + 2 * time_per_beat + time_per_beat)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=80, pitch=38, start=1.5 + time_per_beat, end=1.5 + time_per_beat + time_per_beat)
drum_snare2 = pretty_midi.Note(velocity=80, pitch=38, start=1.5 + 3 * time_per_beat, end=1.5 + 3 * time_per_beat + time_per_beat)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(8):
    start = i * (time_per_beat / 2) + 1.5
    end = start + (time_per_beat / 2)
    note = pretty_midi.Note(velocity=70, pitch=42, start=start, end=end)
    drums.notes.append(note)

# Bar 3: Drums
# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.0 + time_per_beat)
drum_kick2 = pretty_midi.Note(velocity=80, pitch=36, start=3.0 + 2 * time_per_beat, end=3.0 + 2 * time_per_beat + time_per_beat)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=80, pitch=38, start=3.0 + time_per_beat, end=3.0 + time_per_beat + time_per_beat)
drum_snare2 = pretty_midi.Note(velocity=80, pitch=38, start=3.0 + 3 * time_per_beat, end=3.0 + 3 * time_per_beat + time_per_beat)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(8):
    start = i * (time_per_beat / 2) + 3.0
    end = start + (time_per_beat / 2)
    note = pretty_midi.Note(velocity=70, pitch=42, start=start, end=end)
    drums.notes.append(note)

# Bar 4: Drums
# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.5 + time_per_beat)
drum_kick2 = pretty_midi.Note(velocity=80, pitch=36, start=4.5 + 2 * time_per_beat, end=4.5 + 2 * time_per_beat + time_per_beat)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=80, pitch=38, start=4.5 + time_per_beat, end=4.5 + time_per_beat + time_per_beat)
drum_snare2 = pretty_midi.Note(velocity=80, pitch=38, start=4.5 + 3 * time_per_beat, end=4.5 + 3 * time_per_beat + time_per_beat)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(8):
    start = i * (time_per_beat / 2) + 4.5
    end = start + (time_per_beat / 2)
    note = pretty_midi.Note(velocity=70, pitch=42, start=start, end=end)
    drums.notes.append(note)

# Sax: Bar 2-4, your motif. Short, singing, with space.
# Dm7 -> Cm7 -> Bb7. Dm7 is the key. Your motif starts on the 2nd beat of Bar 2.

# Bar 2: Start on beat 2, play D (MIDI 62), rest on beat 3, play C (MIDI 60)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + time_per_beat, end=1.5 + time_per_beat + 0.2),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 2 * time_per_beat, end=1.5 + 2 * time_per_beat + 0.2)
]
sax.notes.extend(sax_notes)

# Bar 3: Play A (MIDI 69) on beat 3, rest on beat 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0 + 2 * time_per_beat, end=3.0 + 2 * time_per_beat + 0.2)
]
sax.notes.extend(sax_notes)

# Bar 4: Play Bb (MIDI 59) on beat 3, rest on beat 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=4.5 + 2 * time_per_beat, end=4.5 + 2 * time_per_beat + 0.2)
]
sax.notes.extend(sax_notes)

# Add instruments to the PrettyMIDI object
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file generated: 'dante_intro.mid'")
