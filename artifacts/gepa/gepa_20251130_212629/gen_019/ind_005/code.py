
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to F minor
# Fm = [F, G, Ab, Bb, C, Db, Eb]
# We're using Fm7 (F, Ab, Bb, Db) as the base chord

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # We'll use this for percussion
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')  # Tenor sax is a close match

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time in seconds per beat
tempo = 160  # BPM
beat_duration = 60.0 / tempo  # 0.375 seconds per beat
bar_duration = 4 * beat_duration  # 1.5 seconds per bar
total_duration = 4 * bar_duration  # 6 seconds total

# Bar 1: Drums alone. Build tension with subtle fills and space.
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0.0 to 1.5s)
# Kick on 1 and 3
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([kick_1, kick_3])

# Snare on 2 and 4
snare_2 = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875)
snare_4 = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625)  # extend slightly to fit in bar 1
drums.notes.extend([snare_2, snare_4])

# Hi-hat on every eighth
hi_hat_notes = []
for i in range(0, 8):
    start = i * 0.1875
    end = start + 0.1875
    hi_hat_notes.append(pretty_midi.Note(velocity=105, pitch=42, start=start, end=end))
drums.notes.extend(hi_hat_notes)

# Bar 2-4: Everyone in. Sax takes a short, hanging motif.

# Bass: Walking line in Fm
# Fm scale: F, G, Ab, Bb, C, Db, Eb
# Chromatic approach, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=65, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=65, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=65, pitch=68, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=65, pitch=69, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=65, pitch=71, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=65, pitch=70, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=65, pitch=72, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=65, pitch=71, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=65, pitch=69, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=65, pitch=68, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=65, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=65, pitch=65, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
# Fm7 = F, Ab, Bb, Db
# Chord on 2 and 4

def chord_notes(root, chord, octave=3):
    intervals = {
        '7': [0, 3, 6, 10],  # 7th chord
    }
    notes = []
    for i in intervals[chord]:
        pitch = root + i
        if pitch > 127:
            pitch -= 12
        notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=0, end=0))
    return notes

# Fm7 on 2 and 4
chord_2 = chord_notes(65, '7')
chord_2[0].start = 2.25
chord_2[0].end = 2.625
chord_2[1].start = 2.25
chord_2[1].end = 2.625
chord_2[2].start = 2.25
chord_2[2].end = 2.625
chord_2[3].start = 2.25
chord_2[3].end = 2.625
piano.notes.extend(chord_2)

chord_4 = chord_notes(65, '7')
chord_4[0].start = 3.75
chord_4[0].end = 4.125
chord_4[1].start = 3.75
chord_4[1].end = 4.125
chord_4[2].start = 3.75
chord_4[2].end = 4.125
chord_4[3].start = 3.75
chord_4[3].end = 4.125
piano.notes.extend(chord_4)

# Drums in bars 2–4
# Kick on 1 and 3
for i in range(2):
    bar_start = 1.5 + i * bar_duration
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    drums.notes.extend([kick_1, kick_3])

# Snare on 2 and 4
for i in range(2):
    bar_start = 1.5 + i * bar_duration
    snare_2 = pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    snare_4 = pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 1.5, end=bar_start + 1.625)
    drums.notes.extend([snare_2, snare_4])

# Hi-hat on every eighth for bars 2–4
for i in range(2):
    bar_start = 1.5 + i * bar_duration
    for j in range(8):
        start = bar_start + j * 0.1875
        end = start + 0.1875
        hi_hat_notes.append(pretty_midi.Note(velocity=105, pitch=42, start=start, end=end))
drums.notes.extend(hi_hat_notes)

# Sax: One short motif — a phrase that *hangs* in the air
# Start on A (69), move to Bb (70), rest, then C (71), rest, then end on Eb (72)

sax_notes = [
    pretty_midi.Note(velocity=105, pitch=69, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=105, pitch=70, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=105, pitch=71, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=105, pitch=72, start=2.625, end=2.75),  # Eb
]
sax.notes.extend(sax_notes)

# Save MIDI file
pm.write('jazz_intro_f_minor.mid')
print("MIDI file written as 'jazz_intro_f_minor.mid'")
