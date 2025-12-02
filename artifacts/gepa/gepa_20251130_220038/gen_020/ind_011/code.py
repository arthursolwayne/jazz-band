
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum mappings
KICK = 36
SNARE = 38
HIHAT = 42

# Time values in seconds
BAR_DURATION = 1.5
BEAT_DURATION = 0.375
HALF_BEAT = 0.1875

# --- Bar 1: Drums only (0.0 - 1.5s) -------------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    # Bar 1
    (KICK, 0.0),
    (SNARE, 0.375),
    (KICK, 0.75),
    (SNARE, 1.125),
    (HIHAT, 0.0),
    (HIHAT, 0.1875),
    (HIHAT, 0.375),
    (HIHAT, 0.5625),
    (HIHAT, 0.75),
    (HIHAT, 0.9375),
    (HIHAT, 1.125),
    (HIHAT, 1.3125),
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# --- Bars 2-4: Full quartet (1.5 - 6.0s) --------------------

def add_note(instrument, pitch, time, duration=0.375):
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# ----------------------------
# Drums (Bars 2-4)
for bar in range(2, 5):
    start_time = (bar - 1) * BAR_DURATION
    
    # Kick on 1 and 3
    add_note(drums, KICK, start_time + 0.0)
    add_note(drums, KICK, start_time + 0.75)
    
    # Snare on 2 and 4
    add_note(drums, SNARE, start_time + 0.375)
    add_note(drums, SNARE, start_time + 1.125)
    
    # Hi-hats on every eighth
    for e in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:
        add_note(drums, HIHAT, start_time + e)

# ----------------------------
# Bass line (Marcus) - Walking line, chromatic approaches
# Fm7: F, Ab, Bb, D
# Bass line in Fm, walking with chromatic passing tones

bass_notes = [
    # Bar 2
    (F, 1.5),
    (Ab, 1.875),
    (Bb, 2.25),
    (D, 2.625),
    (Eb, 2.75),
    (F, 3.0),
    (Ab, 3.375),
    (Bb, 3.75),
    (D, 4.125),
    (Eb, 4.25),
    (F, 4.5),
    (Ab, 4.875),
    (Bb, 5.25),
    (F, 5.625),
]

for pitch, time in bass_notes:
    add_note(bass, pitch, time)

# ----------------------------
# Piano (Diane) - 7th chords, comp on 2 and 4
# F7: F, A, C, Eb
# D7: D, F#, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb

piano_notes = [
    # Bar 2 (comp on 2 and 4)
    (A, 1.875), (C, 1.875), (Eb, 1.875), (F, 1.875),
    (F, 2.625), (A, 2.625), (C, 2.625), (Eb, 2.625),
    # Bar 3 (comp on 2 and 4)
    (F, 3.375), (A, 3.375), (C, 3.375), (Eb, 3.375),
    (G, 4.125), (B, 4.125), (D, 4.125), (F, 4.125),
    # Bar 4 (comp on 2 and 4)
    (C, 4.875), (Eb, 4.875), (G, 4.875), (Bb, 4.875),
    (F, 5.625), (A, 5.625), (C, 5.625), (Eb, 5.625),
]

for pitch, time in piano_notes:
    add_note(piano, pitch, time)

# ----------------------------
# Saxophone (Dante) - Short motif, melodic, leaving it hanging

# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Gb - Bb - C (then resolve in bar 4)
sax_notes = [
    (F, 1.5),
    (Gb, 1.875),
    (Bb, 2.25),
    (C, 2.625),
    (Ab, 3.0),
    (Bb, 3.375),
    (F, 3.75),
    (Gb, 4.125),
    (Bb, 4.5),
    (C, 4.875),
    (F, 5.25),
    (Gb, 5.625),
]

for pitch, time in sax_notes:
    add_note(sax, pitch, time)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write to MIDI file
midi.write("fm_intro_wayne_shorter.midi")
