
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (F, G, A, Bb, B, C, D, Eb)
bass_notes = [
    (78, 1.5),  # F
    (80, 1.875), # G
    (82, 2.25),  # A
    (83, 2.625), # Bb
    (84, 3.0),   # B
    (85, 3.375), # C
    (87, 3.75),  # D
    (88, 4.125), # Eb
    (78, 4.5),   # F
    (80, 4.875), # G
    (82, 5.25),  # A
    (83, 5.625), # Bb
    (84, 6.0)    # B
]
for pitch, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4, comping in F7 (F, A, C, Eb)
# Bar 2: F7 on 2 and 4
piano_notes = [
    (77, 2.0),  # F
    (82, 2.0),  # A
    (84, 2.0),  # C
    (88, 2.0),  # Eb
    (77, 3.0),  # F
    (82, 3.0),  # A
    (84, 3.0),  # C
    (88, 3.0),  # Eb
    (77, 4.0),  # F
    (82, 4.0),  # A
    (84, 4.0),  # C
    (88, 4.0),  # Eb
    (77, 5.0),  # F
    (82, 5.0),  # A
    (84, 5.0),  # C
    (88, 5.0)   # Eb
]
for pitch, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = 1.5 * bar
    kick_time = bar_start
    snare_time = bar_start + 0.375
    hihat_time = bar_start + 0.125
    kick_time2 = bar_start + 0.75
    snare_time2 = bar_start + 1.125
    hihat_time2 = bar_start + 0.375
    hihat_time3 = bar_start + 0.625
    hihat_time4 = bar_start + 0.875
    hihat_time5 = bar_start + 1.125
    hihat_time6 = bar_start + 1.375
    hihat_time7 = bar_start + 1.625
    hihat_time8 = bar_start + 1.875

    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time2, end=kick_time2 + 0.125))

    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time2, end=snare_time2 + 0.125))

    # Hihat on every eighth
    for t in [hihat_time, hihat_time2, hihat_time3, hihat_time4, hihat_time5, hihat_time6, hihat_time7, hihat_time8]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.125))

# Dante: Tenor sax - short motif, F, G, Bb, D (F minor pentatonic, descending)
# Start on 1.5s (bar 2), leave it hanging, come back on bar 3
sax_notes = [
    (77, 1.5),   # F
    (80, 1.875), # G
    (83, 2.25),  # Bb
    (87, 2.625), # D
    (77, 3.5),   # F (return)
    (80, 3.875), # G
    (83, 4.25),  # Bb
    (87, 4.625)  # D
]
for pitch, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
