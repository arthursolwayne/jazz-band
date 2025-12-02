
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instrumets
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time settings (160 BPM, 4/4 time)
beats_per_bar = 4
beat_duration = 0.375  # seconds per beat (60 / 160)
bar_duration = beats_per_bar * beat_duration  # 1.5 seconds per bar

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
bar_start = 0.0
drum_notes = [
    (KICK, bar_start + 0.0),     # kick on beat 1
    (SNARE, bar_start + 0.375),   # snare on beat 2
    (KICK, bar_start + 0.75),     # kick on beat 3
    (SNARE, bar_start + 1.125),   # snare on beat 4
    (HIHAT, bar_start + 0.0),     # hihat on beat 1
    (HIHAT, bar_start + 0.1875),  # hihat on & of 1
    (HIHAT, bar_start + 0.375),   # hihat on beat 2
    (HIHAT, bar_start + 0.5625),  # hihat on & of 2
    (HIHAT, bar_start + 0.75),    # hihat on beat 3
    (HIHAT, bar_start + 0.9375),  # hihat on & of 3
    (HIHAT, bar_start + 1.125),   # hihat on beat 4
    (HIHAT, bar_start + 1.3125),  # hihat on & of 4
]

for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2-4 (1.5 - 6.0s) - Full quartet
bar_start = 1.5

# Marcus: Walking bass line in Dm (D, F, G, C), chromatic approaches, no repeats
bass_notes = [
    # Bar 2: D -> F -> G -> C
    (62, bar_start + 0.0),    # D (root)
    (64, bar_start + 0.375),  # F (3rd)
    (67, bar_start + 0.75),   # G (5th)
    (67, bar_start + 1.125),  # C (7th)

    # Bar 3: D -> C -> D -> F
    (62, bar_start + 1.5),    # D
    (60, bar_start + 1.875),  # C (chromatic approach)
    (62, bar_start + 2.25),   # D
    (64, bar_start + 2.625),  # F

    # Bar 4: D -> F -> G -> C
    (62, bar_start + 3.0),    # D
    (64, bar_start + 3.375),  # F
    (67, bar_start + 3.75),   # G
    (67, bar_start + 4.125),  # C
]

for note_number, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: Comping on 2 and 4 with 7th chords (Dm7 = D, F, A, C)
# Dm7 = D (62), F (64), A (69), C (60)
# Play on 2 and 4 (beat 2 and beat 4 of each bar)
piano_notes = [
    # Bar 2: Dm7 on beat 2
    (62, bar_start + 0.375),   # D
    (64, bar_start + 0.375),   # F
    (69, bar_start + 0.375),   # A
    (60, bar_start + 0.375),   # C

    # Bar 2: Dm7 on beat 4
    (62, bar_start + 1.125),
    (64, bar_start + 1.125),
    (69, bar_start + 1.125),
    (60, bar_start + 1.125),

    # Bar 3: Dm7 on beat 2
    (62, bar_start + 1.875),
    (64, bar_start + 1.875),
    (69, bar_start + 1.875),
    (60, bar_start + 1.875),

    # Bar 3: Dm7 on beat 4
    (62, bar_start + 2.625),
    (64, bar_start + 2.625),
    (69, bar_start + 2.625),
    (60, bar_start + 2.625),

    # Bar 4: Dm7 on beat 2
    (62, bar_start + 3.375),
    (64, bar_start + 3.375),
    (69, bar_start + 3.375),
    (60, bar_start + 3.375),

    # Bar 4: Dm7 on beat 4
    (62, bar_start + 4.125),
    (64, bar_start + 4.125),
    (69, bar_start + 4.125),
    (60, bar_start + 4.125),
]

for note_number, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.25)
    piano.notes.append(note)

# Dante: Tenor Sax motif (Dm scale, no scale runs)
# Motif: D, F, G, D (start), then leave it hanging
# Repeat the motif slightly altered at the end

# Bar 2 (1.5s)
sax_notes = [
    (62, bar_start + 0.0),  # D
    (64, bar_start + 0.375),  # F
    (67, bar_start + 0.75),   # G
    (62, bar_start + 1.125),  # D

    # Bar 3 (3.0s)
    (67, bar_start + 1.5),    # G
    (64, bar_start + 1.875),  # F
    (62, bar_start + 2.25),   # D
    (64, bar_start + 2.625),  # F

    # Bar 4 (4.5s)
    (67, bar_start + 3.0),    # G
    (64, bar_start + 3.375),  # F
    (62, bar_start + 3.75),   # D
    (62, bar_start + 4.125),  # D (hanging on last beat)
]

for note_number, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
