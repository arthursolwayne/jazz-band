
import pretty_midi
import numpy as np

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set key signature to F major (no sharps or flats)
pm.key_signature_changes = [pretty_midi.KeySignature(0, 0, 0.0)]  # F major

# Define time per bar (in seconds)
time_per_bar = 1.5  # 160 BPM, 4/4 time
bar_length = time_per_bar
total_time = 4 * bar_length

# == Drums ==
drums_program = pretty_midi.instrument_name_to_program('Drums')
drum_inst = pretty_midi.Instrument(program=drums_program)

# Kick on 1 and 3
for bar in range(4):
    kick_time = bar * bar_length + 0.0
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drum_inst.notes.append(kick_note)

    kick_time = bar * bar_length + 0.75
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drum_inst.notes.append(kick_note)

# Snare on 2 and 4
for bar in range(4):
    snare_time = bar * bar_length + 0.5
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drum_inst.notes.append(snare_note)

    snare_time = bar * bar_length + 1.25
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drum_inst.notes.append(snare_note)

# Hi-hat on every eighth note
for bar in range(4):
    for i in range(8):
        hi_hat_time = bar * bar_length + i * 0.1875
        hi_hat_note = pretty_midi.Note(velocity=90, pitch=42, start=hi_hat_time, end=hi_hat_time + 0.05)
        drum_inst.notes.append(hi_hat_note)

# Add fills in bar 2 and 4
for bar in [1, 3]:
    fill_time = bar * bar_length + 1.5
    fill_note = pretty_midi.Note(velocity=100, pitch=38, start=fill_time, end=fill_time + 0.1)
    drum_inst.notes.append(fill_note)
    fill_note = pretty_midi.Note(velocity=100, pitch=42, start=fill_time + 0.25, end=fill_time + 0.3)
    drum_inst.notes.append(fill_note)

pm.instruments.append(drum_inst)

# == Bass ==
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass_inst = pretty_midi.Instrument(program=bass_program)

# Walking line in F major, roots and fifths with chromatic approaches
# Starting from D2 (root of F major key center)
for bar in range(4):
    time = bar * bar_length
    # Bar 1: D2 -> F2
    bass_note = pretty_midi.Note(velocity=80, pitch=38, start=time + 0.0, end=time + 0.1)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=40, start=time + 0.25, end=time + 0.35)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=38, start=time + 0.5, end=time + 0.6)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=40, start=time + 0.75, end=time + 0.85)
    bass_inst.notes.append(bass_note)

    # Bar 2: Bb2 -> C3
    bass_note = pretty_midi.Note(velocity=80, pitch=41, start=time + 1.5, end=time + 1.6)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=43, start=time + 1.75, end=time + 1.85)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=41, start=time + 2.0, end=time + 2.1)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=43, start=time + 2.25, end=time + 2.35)
    bass_inst.notes.append(bass_note)

    # Bar 3: F2 -> G2
    bass_note = pretty_midi.Note(velocity=80, pitch=38, start=time + 3.0, end=time + 3.1)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=40, start=time + 3.25, end=time + 3.35)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=38, start=time + 3.5, end=time + 3.6)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=40, start=time + 3.75, end=time + 3.85)
    bass_inst.notes.append(bass_note)

    # Bar 4: C3 -> F2
    bass_note = pretty_midi.Note(velocity=80, pitch=43, start=time + 4.5, end=time + 4.6)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=40, start=time + 4.75, end=time + 4.85)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=43, start=time + 5.0, end=time + 5.1)
    bass_inst.notes.append(bass_note)
    bass_note = pretty_midi.Note(velocity=80, pitch=38, start=time + 5.25, end=time + 5.35)
    bass_inst.notes.append(bass_note)

pm.instruments.append(bass_inst)

# == Piano ==
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_inst = pretty_midi.Instrument(program=piano_program)

# Open voicings, resolve on last beat
# Bar 1: Fmaj7 -> Fmaj7
piano_notes = [65, 68, 72, 76]  # Fmaj7
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=0.0, end=0.4)
    piano_inst.notes.append(piano_note)

# Bar 2: Gm7 -> Gm7
piano_notes = [67, 70, 74, 76]  # Gm7
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=1.5, end=1.9)
    piano_inst.notes.append(piano_note)

# Bar 3: Cmaj7 -> Cmaj7
piano_notes = [60, 64, 68, 72]  # Cmaj7
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=3.0, end=3.4)
    piano_inst.notes.append(piano_note)

# Bar 4: Dm7 -> Fmaj7
piano_notes = [62, 65, 69, 72]  # Dm7 (resolve to Fmaj7)
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=4.5, end=4.9)
    piano_inst.notes.append(piano_note)

# Add a final Fmaj7 chord to resolve
piano_notes = [65, 68, 72, 76]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=5.0, end=5.1)
    piano_inst.notes.append(piano_note)

pm.instruments.append(piano_inst)

# == Tenor Sax ==
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_inst = pretty_midi.Instrument(program=sax_program)

# Motif: F - A - Bb - G (F major, with a chromatic approach)
# Start on beat 1, end on beat 4, leave it hanging, then resolve

# First motif (beat 1)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=0.0, end=0.2)
sax_inst.notes.append(sax_note)

# Beat 2: rest
# Beat 3: rest

# Beat 4: repeat motif, resolve on F
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.7)
sax_inst.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=68, start=1.7, end=1.9)
sax_inst.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=69, start=1.9, end=2.1)
sax_inst.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=2.1, end=2.3)
sax_inst.notes.append(sax_note)

# Leave it hanging until beat 4 of the final bar
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.2)
sax_inst.notes.append(sax_note)

pm.instruments.append(sax_inst)

# Save the MIDI file
pm.write("jazz_intro_dante.mid")
print("MIDI file 'jazz_intro_dante.mid' has been created.")
