
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new MIDI file
pm = pretty_midi.PrettyMIDIClass()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Set up instruments
drums_inst = Instrument(program=10, is_drum=True, name='Drums')
bass_inst = Instrument(program=33, name='Bass')
piano_inst = Instrument(program=0, name='Piano')
sax_inst = Instrument(program=64, name='Saxophone')

# Add instruments to the MIDI file
pm.instruments = [drums_inst, bass_inst, piano_inst, sax_inst]

# Utilities
def add_note(inst, pitch, start, end, velocity):
    note = Note(pitch, start, end, velocity)
    inst.notes.append(note)

# 160 BPM = 60 / 160 = 0.375 seconds per beat
beat = 0.375
bar = 4 * beat  # 1.5 seconds per bar

# DRUMS - Little Ray
# Kick on 1 & 3, snare on 2 & 4, hihat on every 8th
for bar_num in range(4):
    bar_start = bar_num * bar
    kick_times = [bar_start + 0 * beat, bar_start + 2 * beat]
    snare_times = [bar_start + 1 * beat, bar_start + 3 * beat]
    hihat_times = [bar_start + i * beat / 2 for i in range(8)]

    for t in kick_times:
        add_note(drums_inst, 36, t, t + 0.1, 100)
    for t in snare_times:
        add_note(drums_inst, 38, t, t + 0.1, 100)
    for t in hihat_times:
        add_note(drums_inst, 42, t, t + 0.05, 80)

# BASS - Marcus
# Walking line with chromatic approaches
bass_notes = [
    (62, 0), (63, 0.25), (64, 0.5), (63, 0.75),  # Dm7: F, D, C, Bb
    (62, 1), (60, 1.25), (61, 1.5), (60, 1.75),  # Dm7: F, D, C, Bb
    (62, 2), (63, 2.25), (64, 2.5), (63, 2.75),  # Dm7: F, D, C, Bb
    (62, 3), (60, 3.25), (61, 3.5), (60, 3.75)   # Dm7: F, D, C, Bb
]

for pitch, time in bass_notes:
    add_note(bass_inst, pitch, time, time + 0.25, 100)

# PIANO - Diane
# Sparse 7th chords on 2 and 4
# Dm7: D, F, A, C
# F7: F, A, C, E
# G7: G, B, D, F
# C7: C, E, G, B

for bar_num in range(4):
    bar_start = bar_num * bar
    # 2nd beat: F7
    add_note(piano_inst, 65, bar_start + 1 * beat, bar_start + 1.25 * beat, 100)
    add_note(piano_inst, 68, bar_start + 1 * beat, bar_start + 1.25 * beat, 100)
    add_note(piano_inst, 67, bar_start + 1 * beat, bar_start + 1.25 * beat, 100)
    add_note(piano_inst, 69, bar_start + 1 * beat, bar_start + 1.25 * beat, 100)

    # 4th beat: C7
    add_note(piano_inst, 60, bar_start + 3 * beat, bar_start + 3.25 * beat, 100)
    add_note(piano_inst, 64, bar_start + 3 * beat, bar_start + 3.25 * beat, 100)
    add_note(piano_inst, 67, bar_start + 3 * beat, bar_start + 3.25 * beat, 100)
    add_note(piano_inst, 71, bar_start + 3 * beat, bar_start + 3.25 * beat, 100)

# SAX - Dante
# A short motif, ends on C (unresolved)
sax_notes = [
    (62, 0), (64, 0.5), (62, 1), (60, 1.5),  # D, F, D, C
]

for pitch, time in sax_notes:
    add_note(sax_inst, pitch, time, time + 0.5, 110)

# Save the MIDI file
pm.write('dante_russo_intro.mid')
print("MIDI file written: 'dante_russo_intro.mid'")
