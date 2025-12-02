
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, piano, bass, sax]

# Define constants
BPM = 160
BEAT = 60 / BPM
BAR = 4 * BEAT
NOTE_DURATION = BEAT / 4  # 16th note
REST_DURATION = BEAT / 2  # 8th note rest

# Bar 1: Drums alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0
bar_1_end = bar_1_start + BAR

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_1_start, end=bar_1_start + NOTE_DURATION))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_1_start + 2 * NOTE_DURATION, end=bar_1_start + 2 * NOTE_DURATION + NOTE_DURATION))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_1_start + NOTE_DURATION, end=bar_1_start + NOTE_DURATION + NOTE_DURATION))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_1_start + 3 * NOTE_DURATION, end=bar_1_start + 3 * NOTE_DURATION + NOTE_DURATION))

# Hi-hats on every eighth
for i in range(8):
    start = bar_1_start + i * NOTE_DURATION
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + NOTE_DURATION))

# Bar 2: All instruments join in

bar_2_start = bar_1_end
bar_2_end = bar_2_start + BAR

# Bass (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # F (1st beat)
    (17, bar_2_start, bar_2_start + NOTE_DURATION),
    # Bb (2nd beat) - chromatic approach to Bb
    (16, bar_2_start + NOTE_DURATION, bar_2_start + 2 * NOTE_DURATION),
    # Bb (3rd beat)
    (17, bar_2_start + 2 * NOTE_DURATION, bar_2_start + 3 * NOTE_DURATION),
    # D (4th beat) - chromatic approach to D
    (15, bar_2_start + 3 * NOTE_DURATION, bar_2_start + 4 * NOTE_DURATION),
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: 7th chord on 2 and 4
    # F7 on 2nd beat: F A C Eb
    (53, bar_2_start + NOTE_DURATION, bar_2_start + 2 * NOTE_DURATION),
    (58, bar_2_start + NOTE_DURATION, bar_2_start + 2 * NOTE_DURATION),
    (60, bar_2_start + NOTE_DURATION, bar_2_start + 2 * NOTE_DURATION),
    (62, bar_2_start + NOTE_DURATION, bar_2_start + 2 * NOTE_DURATION),
    # F7 on 4th beat
    (53, bar_2_start + 3 * NOTE_DURATION, bar_2_start + 4 * NOTE_DURATION),
    (58, bar_2_start + 3 * NOTE_DURATION, bar_2_start + 4 * NOTE_DURATION),
    (60, bar_2_start + 3 * NOTE_DURATION, bar_2_start + 4 * NOTE_DURATION),
    (62, bar_2_start + 3 * NOTE_DURATION, bar_2_start + 4 * NOTE_DURATION),
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=end))

# Sax (Dante): Motif in F, one short phrase, hanging on the last note
motif_start = bar_2_start
motif_notes = [
    # F (beat 1) - long note
    (60, motif_start, motif_start + NOTE_DURATION * 2),
    # Ab (beat 2) - short
    (62, motif_start + NOTE_DURATION * 2, motif_start + NOTE_DURATION * 3),
    # Bb (beat 3) - short
    (62, motif_start + NOTE_DURATION * 3, motif_start + NOTE_DURATION * 4),
    # Unresolved ending (beat 4) - rest
    (60, motif_start + NOTE_DURATION * 4, motif_start + NOTE_DURATION * 5),  # sustained but not released
]
# Only render the first three notes
for i in range(3):
    pitch, start, end = motif_notes[i]
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end))

# Add a rest in the last bar for the unresolved ending
sax.notes.append(pretty_midi.Note(velocity=0, pitch=60, start=motif_start + NOTE_DURATION * 4, end=motif_start + NOTE_DURATION * 5))

# Bar 3: Silence - build tension
bar_3_start = bar_2_end
bar_3_end = bar_3_start + BAR

# All instruments rest
pass  # No notes in this bar

# Bar 4: Distant echo of the motif — a question, not a statement
bar_4_start = bar_3_end
bar_4_end = bar_4_start + BAR

# Sax: Echo of the motif, but incomplete
echo_notes = [
    # F (beat 1)
    (60, bar_4_start, bar_4_start + NOTE_DURATION * 0.5),
    # Ab (beat 2)
    (62, bar_4_start + NOTE_DURATION, bar_4_start + NOTE_DURATION * 1.5),
]
for pitch, start, end in echo_notes:
    sax.notes.append(pretty_midi.Note(velocity=75, pitch=pitch, start=start, end=end))

# Piano: Single note on 2 and 4 — unresolved chord
piano.notes.append(pretty_midi.Note(velocity=70, pitch=60, start=bar_4_start + NOTE_DURATION, end=bar_4_start + NOTE_DURATION + NOTE_DURATION))
piano.notes.append(pretty_midi.Note(velocity=70, pitch=60, start=bar_4_start + 3 * NOTE_DURATION, end=bar_4_start + 3 * NOTE_DURATION + NOTE_DURATION))

# Bass: Rest, but implied walking line
pass  # No notes

# Drums: Light fill on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_4_start + NOTE_DURATION, end=bar_4_start + NOTE_DURATION + NOTE_DURATION))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=bar_4_start + 3 * NOTE_DURATION, end=bar_4_start + 3 * NOTE_DURATION + NOTE_DURATION))

# Write the MIDI file
pm.write('dante_russo_intro.mid')
print("MIDI file generated as 'dante_russo_intro.mid'")
