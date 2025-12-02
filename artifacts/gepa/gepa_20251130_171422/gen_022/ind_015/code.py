
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to D minor (key number 20 in MIDI)
key = 20  # D minor

# Create an instrument for the drums
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drum_inst = pretty_midi.Instrument(program=drum_program)
pm.instruments.append(drum_inst)

# Create an instrument for the piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_inst = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_inst)

# Create an instrument for the bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass_inst = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_inst)

# Create an instrument for the tenor sax (you)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_inst = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_inst)

# Define note durations based on 160 BPM (each beat = 0.375 seconds)
# Each bar is 6 seconds (4 bars = 24 seconds total)

# Define the tempo
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0, tempo=160)]

# Define note values in terms of time (seconds)
note_duration = 0.375  # 1 beat

# Define D minor scale (notes in MIDI numbers)
Dm_notes = [62, 64, 65, 67, 69, 70, 72]  # D, Eb, F, G, A, Bb, C

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0
bar1_end = 6

# Kick on 1 and 3 (beats 0 and 2)
for beat in [0, 2]:
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + beat * note_duration, end=bar1_start + beat * note_duration + 0.1)
    drum_inst.notes.append(kick_note)

# Snare on 2 and 4 (beats 1 and 3)
for beat in [1, 3]:
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + beat * note_duration, end=bar1_start + beat * note_duration + 0.1)
    drum_inst.notes.append(snare_note)

# Hihat on every eighth note
for i in range(0, 8):
    hihat_note = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + (i / 2) * note_duration, end=bar1_start + (i / 2) * note_duration + 0.1)
    drum_inst.notes.append(hihat_note)

# Bar 2: Everyone enters. Start of the motif (you on sax)
bar2_start = 6
bar2_end = 12

# Tenor sax motif - one short phrase with tension and release
# Motif: D (62), F (65), G (67), D (62) - ascending then resolving
# Introduce a space after the third note, then resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=bar2_start, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=65, start=bar2_start + 0.75, end=bar2_start + 1.5),
    pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 1.5, end=bar2_start + 2.25),
    pretty_midi.Note(velocity=110, pitch=62, start=bar2_start + 2.25, end=bar2_start + 3.0)
]
sax_inst.notes.extend(sax_notes)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start, end=bar2_start + 0.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=bar2_start + 0.75, end=bar2_start + 1.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start + 1.5, end=bar2_start + 2.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 2.25, end=bar2_start + 3.0)   # G
]
bass_inst.notes.extend(bass_notes)

# Piano (Diane) - comping on 2 and 4, 7th chords
piano_notes = [
    # Bar 2, beat 2: Dm7 (D, F, A, C) on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 1.0, end=bar2_start + 1.5),
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 1.0, end=bar2_start + 1.5),
    pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + 1.0, end=bar2_start + 1.5),
    pretty_midi.Note(velocity=90, pitch=72, start=bar2_start + 1.0, end=bar2_start + 1.5),

    # Bar 2, beat 4: Dm7 (same chord) on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 3.0, end=bar2_start + 3.5),
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 3.0, end=bar2_start + 3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + 3.0, end=bar2_start + 3.5),
    pretty_midi.Note(velocity=90, pitch=72, start=bar2_start + 3.0, end=bar2_start + 3.5)
]
piano_inst.notes.extend(piano_notes)

# Bar 3: Continue the motif (you on sax)
bar3_start = 12
bar3_end = 18

# Continue the motif with a slight variation or space
# D (62), A (69), Bb (70), then stop — a pause before the resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=bar3_start, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=69, start=bar3_start + 0.75, end=bar3_start + 1.5),
    pretty_midi.Note(velocity=110, pitch=70, start=bar3_start + 1.5, end=bar3_start + 2.25),
    pretty_midi.Note(velocity=110, pitch=62, start=bar3_start + 2.25, end=bar3_start + 3.0)
]
sax_inst.notes.extend(sax_notes)

# Bass continues with walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=bar3_start, end=bar3_start + 0.75),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=bar3_start + 0.75, end=bar3_start + 1.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=bar3_start + 1.5, end=bar3_start + 2.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=bar3_start + 2.25, end=bar3_start + 3.0)   # D
]
bass_inst.notes.extend(bass_notes)

# Piano continues comping on 2 and 4
piano_notes = [
    # Bar 3, beat 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=bar3_start + 1.0, end=bar3_start + 1.5),
    pretty_midi.Note(velocity=90, pitch=65, start=bar3_start + 1.0, end=bar3_start + 1.5),
    pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + 1.0, end=bar3_start + 1.5),
    pretty_midi.Note(velocity=90, pitch=72, start=bar3_start + 1.0, end=bar3_start + 1.5),

    # Bar 3, beat 4: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=bar3_start + 3.0, end=bar3_start + 3.5),
    pretty_midi.Note(velocity=90, pitch=65, start=bar3_start + 3.0, end=bar3_start + 3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + 3.0, end=bar3_start + 3.5),
    pretty_midi.Note(velocity=90, pitch=72, start=bar3_start + 3.0, end=bar3_start + 3.5)
]
piano_inst.notes.extend(piano_notes)

# Bar 4: Resolution (you on sax)
bar4_start = 18
bar4_end = 24

# Resolve the motif with a descending line or space
# D (62), C (72), Bb (70), rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=bar4_start, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=72, start=bar4_start + 0.75, end=bar4_start + 1.5),
    pretty_midi.Note(velocity=110, pitch=70, start=bar4_start + 1.5, end=bar4_start + 2.25),
    pretty_midi.Note(velocity=110, pitch=62, start=bar4_start + 2.25, end=bar4_start + 3.0)
]
sax_inst.notes.extend(sax_notes)

# Bass continues with walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar4_start, end=bar4_start + 0.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.5),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=bar4_start + 1.5, end=bar4_start + 2.25),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=bar4_start + 2.25, end=bar4_start + 3.0)   # Bb
]
bass_inst.notes.extend(bass_notes)

# Piano continues comping on 2 and 4
piano_notes = [
    # Bar 4, beat 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + 1.0, end=bar4_start + 1.5),
    pretty_midi.Note(velocity=90, pitch=65, start=bar4_start + 1.0, end=bar4_start + 1.5),
    pretty_midi.Note(velocity=90, pitch=69, start=bar4_start + 1.0, end=bar4_start + 1.5),
    pretty_midi.Note(velocity=90, pitch=72, start=bar4_start + 1.0, end=bar4_start + 1.5),

    # Bar 4, beat 4: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + 3.0, end=bar4_start + 3.5),
    pretty_midi.Note(velocity=90, pitch=65, start=bar4_start + 3.0, end=bar4_start + 3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=bar4_start + 3.0, end=bar4_start + 3.5),
    pretty_midi.Note(velocity=90, pitch=72, start=bar4_start + 3.0, end=bar4_start + 3.5)
]
piano_inst.notes.extend(piano_notes)

# Add drum fill for the end, slight cymbal crash
cymbal_note = pretty_midi.Note(velocity=100, pitch=46, start=bar4_start + 3.0, end=bar4_start + 3.1)
drum_inst.notes.append(cymbal_note)

# Write the MIDI file
pm.write("dante_intro.mid")
print("MIDI file generated: 'dante_intro.mid'")
