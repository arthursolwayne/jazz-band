
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (36, 1.125, 0.375),# Kick on 3
    (38, 1.5, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # C#
    (63, 2.25, 0.375),  # D#
    (64, 2.625, 0.375), # E
    (65, 2.875, 0.375), # F
    (67, 3.25, 0.375),  # G
    (68, 3.625, 0.375), # G#
    (70, 4.0, 0.375),   # A
    (71, 4.375, 0.375), # A#
    (72, 4.75, 0.375),  # B
    (71, 5.125, 0.375), # A#
    (70, 5.5, 0.375),   # A
    (68, 5.875, 0.375)  # G#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.875, 0.375), # E7: E, G#, B, D
    (69, 1.875, 0.375),
    (71, 1.875, 0.375),
    (67, 1.875, 0.375),
    # Bar 3
    (67, 3.125, 0.375), # G7: G, B, D, F
    (71, 3.125, 0.375),
    (74, 3.125, 0.375),
    (69, 3.125, 0.375),
    # Bar 4
    (64, 4.375, 0.375), # E7 again
    (69, 4.375, 0.375),
    (71, 4.375, 0.375),
    (67, 4.375, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick
    kick_start = bar_start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    drums.notes.append(kick)
    kick_start = bar_start + 1.125
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    drums.notes.append(kick)
    # Snare
    snare_start = bar_start + 0.75
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    drums.notes.append(snare)
    snare_start = bar_start + 1.5
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    drums.notes.append(snare)
    # Hihat
    for i in range(4):
        hihat_start = bar_start + i * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.375)
        drums.notes.append(hihat)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C (60), E (64), B (71), C (60) - start on bar 2, leave on bar 3, return on bar 4

# Bar 2
sax_notes = [
    (60, 1.5, 0.375),   # C
    (64, 1.875, 0.375), # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4
sax_notes = [
    (71, 4.0, 0.375),   # B
    (60, 4.375, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
