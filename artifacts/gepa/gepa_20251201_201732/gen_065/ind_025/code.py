
import pretty_midi

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key (F minor)
key_number = pretty_midi.key_number_from_name('F minor')

# Define instrument tracks
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Sax')

# Create instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Define timing (160 BPM, 4/4 time)
seconds_per_beat = 60.0 / 160
bar_length = 4 * seconds_per_beat  # 4 bars = 6 seconds

# 1. Bar 1: Drums only
# Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
for beat in range(4):
    time = beat * seconds_per_beat
    if beat % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)

for eighth in range(8):
    time = (eighth * seconds_per_beat / 2)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# 2. Bar 2: Bass enters (Walking line in F minor)
# Fm7: F, Ab, C, Eb
# Walking line: G - F - Ab - G - Bb - Ab - Bb - B
walk = [60, 59, 61, 60, 62, 61, 62, 63]  # G, F, Ab, G, Bb, Ab, Bb, B
for i, pitch in enumerate(walk):
    time = (i + 1) * seconds_per_beat / 8
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# 3. Bar 3: Piano enters (Open voicings, resolving chords)
# Fm7, Bb7, Eb7, Ab7
chords = {
    0: [25, 28, 30, 32],  # Fm7 (F, Ab, C, Eb)
    1: [23, 26, 28, 31],  # Bb7 (Bb, D, F, Ab)
    2: [21, 24, 26, 29],  # Eb7 (Eb, G, Bb, D)
    3: [19, 22, 24, 27]   # Ab7 (Ab, C, Eb, G)
}

for bar in range(4):
    time = bar * seconds_per_beat
    for note in chords[bar]:
        note_obj = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(note_obj)

# 4. Bar 4: Sax enters (Short motif, lingering question)
# Motif: F - Ab - Bb - Eb (Fm7 chord, but played as a melody)
melody = [60, 61, 62, 64]  # F, Ab, Bb, Eb
for i, pitch in enumerate(melody):
    time = (i + 1) * seconds_per_beat / 4  # spaced evenly across the bar
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Write the MIDI file
pm.write('jazz_intro.mid')
