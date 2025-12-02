
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object with 160 BPM (4/4 time)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key: D minor (D, F, G)
key = 'Dm'

# Define time per bar (160 BPM => 60/160 seconds per beat)
# 4/4 time => 4 beats per bar
# 1 bar = 4 / 160 * 60 = 1.5 seconds
BAR_DURATION = 1.5
BEAT_DURATION = BAR_DURATION / 4  # 0.375 seconds

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Add instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# 1. DRUMS: Bar 1 (Little Ray)
# Kick on 1 and 3, hihat on every eighth, fill on beat 4

# Kick: beat 0 and 2
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0, end=BEAT_DURATION),
              pretty_midi.Note(velocity=100, pitch=36, start=2 * BEAT_DURATION, end=3 * BEAT_DURATION)]

# Hihat: every 8th
hihat_notes = [pretty_midi.Note(velocity=90, pitch=42, start=i * 0.1875, end=i * 0.1875 + 0.1875)
               for i in range(0, int(BAR_DURATION / 0.1875))]

# Fill on beat 4: 32nd notes
fill_notes = [pretty_midi.Note(velocity=85, pitch=38, start=3.75, end=3.875),
              pretty_midi.Note(velocity=85, pitch=40, start=3.875, end=4.0),
              pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.0)]

for n in kick_notes + hihat_notes + fill_notes:
    drums.notes.append(n)

# 2. BASS: Walking line in Dm (D2-G2), roots and fifths with chromatic approaches
# Dm = D, F, Ab, C (but we're using D2-G2 as the bass range)
# Bar 1 (0–1.5s): D2, F2, D2, C2, Ab2, F2, D2, D2

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=0.0, end=0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=0.375, end=0.75), # F2
    pretty_midi.Note(velocity=80, pitch=50, start=0.75, end=1.125),  # D2
    pretty_midi.Note(velocity=80, pitch=52, start=1.125, end=1.5),  # C2
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.875),  # Ab2
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # D2
]

# Bar 2 (3.0–4.5s): D2, F2, G2, Ab2, D2, F2, G2, C2
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=53, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0)
])

for n in bass_notes:
    bass.notes.append(n)

# 3. PIANO: Open voicings, resolve on the last beat of each bar
# Bar 1 (0–1.5s): Dm7 (D, F, Ab, C) -> F7 (F, A, C, Eb) -> Gm7 (G, Bb, D, F) -> C7 (C, E, G, Bb)
# Bar 2 (1.5–3.0s): Dm7 -> D9 -> F7 -> Gm7
# Bar 3 (3.0–4.5s): C7 -> G7 -> Cmaj7 -> Dm7
# Bar 4 (4.5–6.0s): Dm7 -> Dm9 -> F7 -> Gm7

def add_piano_notes(start_time, chords):
    for idx, chord in enumerate(chords):
        note_times = [start_time + i * 0.75 for i in range(4)]
        for pitch in chord:
            piano.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=note_times[0], end=note_times[-1]))
        # Add a rest on the 3rd note of the bar (3rd beat), then resolve
        if idx < len(chords) - 1:
            rest = pretty_midi.Note(velocity=0, pitch=0, start=note_times[2], end=note_times[2] + 0.125)
            piano.notes.append(rest)

# Define chords
bar1_chords = [[62, 64, 67, 69],  # Dm7
               [65, 68, 71, 72],   # F7
               [67, 71, 74, 76],   # Gm7
               [60, 64, 67, 71]]   # C7

bar2_chords = [[62, 64, 67, 69],  # Dm7
               [62, 64, 67, 71],   # D9
               [65, 68, 71, 72],   # F7
               [67, 71, 74, 76]]   # Gm7

bar3_chords = [[60, 64, 67, 71],  # C7
               [67, 71, 74, 76],   # G7
               [60, 64, 67, 72],   # Cmaj7
               [62, 64, 67, 69]]   # Dm7

bar4_chords = [[62, 64, 67, 69],  # Dm7
               [62, 64, 67, 71],   # D9
               [65, 68, 71, 72],   # F7
               [67, 71, 74, 76]]   # Gm7

# Add piano chords over the 4 bars
add_piano_notes(0, bar1_chords)
add_piano_notes(1.5, bar2_chords)
add_piano_notes(3.0, bar3_chords)
add_piano_notes(4.5, bar4_chords)

# 4. SAX: Motif — start, leave it hanging, finish
# Motif: D (62), F (64), G (67), D (62), with rests and syncopation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.75), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.5)    # D (resolve)
]

for n in sax_notes:
    sax.notes.append(n)

# Save the MIDI
pm.write('wayne_intro.mid')

print("MIDI file created: 'wayne_intro.mid'")
print("Ready to make Wayne lean forward.")
