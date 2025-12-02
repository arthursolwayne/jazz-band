
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
    (36, 0.0, 0.375),
    (42, 0.0, 0.125),
    (38, 0.375, 0.375),
    (42, 0.375, 0.125),
    (36, 0.75, 0.375),
    (42, 0.75, 0.125),
    (38, 1.125, 0.375),
    (42, 1.125, 0.125),
    (42, 1.5, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches, never the same note twice
bass_notes = [
    (64, 1.5, 0.375),  # F
    (65, 1.875, 0.375), # F#
    (67, 2.25, 0.375),  # G
    (69, 2.625, 0.375), # G#
    (71, 3.0, 0.375),   # A
    (72, 3.375, 0.375), # A#
    (73, 3.75, 0.375),  # Bb
    (74, 4.125, 0.375), # B
    (76, 4.5, 0.375),   # C
    (77, 4.875, 0.375), # C#
    (79, 5.25, 0.375),  # D
    (81, 5.625, 0.375)  # D#
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (64, 1.5, 0.375),  # F7
    (69, 1.5, 0.375),
    (72, 1.5, 0.375),
    (76, 1.5, 0.375),
    (69, 2.25, 0.375),
    (72, 2.25, 0.375),
    (76, 2.25, 0.375),
    (80, 2.25, 0.375),

    # Bar 3 (3.0 - 4.5s)
    (64, 3.0, 0.375),  # F7
    (69, 3.0, 0.375),
    (72, 3.0, 0.375),
    (76, 3.0, 0.375),
    (69, 3.75, 0.375),
    (72, 3.75, 0.375),
    (76, 3.75, 0.375),
    (80, 3.75, 0.375),

    # Bar 4 (4.5 - 6.0s)
    (64, 4.5, 0.375),  # F7
    (69, 4.5, 0.375),
    (72, 4.5, 0.375),
    (76, 4.5, 0.375),
    (69, 5.25, 0.375),
    (72, 5.25, 0.375),
    (76, 5.25, 0.375),
    (80, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax - sparse, expressive motif, start and finish it
# Bar 2: Start the motif
sax_notes = [
    (64, 1.5, 0.25),   # F
    (67, 1.75, 0.25),  # G
    (64, 2.0, 0.25),   # F (rest)
    (69, 2.25, 0.25),  # G#
    (67, 2.5, 0.25),   # G
    (64, 2.75, 0.25),  # F
    (66, 3.0, 0.25),   # F#
    (64, 3.25, 0.25),  # F

    # Bar 3: Continue the motif
    (69, 3.5, 0.25),   # G#
    (67, 3.75, 0.25),  # G
    (64, 4.0, 0.25),   # F
    (66, 4.25, 0.25),  # F#
    (69, 4.5, 0.25),   # G#
    (67, 4.75, 0.25),  # G
    (64, 5.0, 0.25),   # F
    (66, 5.25, 0.25),  # F#

    # Bar 4: Resolve the motif
    (64, 5.5, 0.25),   # F
    (67, 5.75, 0.25),  # G
    (64, 6.0, 0.25)    # F
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Add hi-hat rhythm for Little Ray in bars 2-4
hi_hat_notes = [
    (42, 1.5, 0.125),
    (42, 1.625, 0.125),
    (42, 1.75, 0.125),
    (42, 1.875, 0.125),
    (42, 2.0, 0.125),
    (42, 2.125, 0.125),
    (42, 2.25, 0.125),
    (42, 2.375, 0.125),
    (42, 2.5, 0.125),
    (42, 2.625, 0.125),
    (42, 2.75, 0.125),
    (42, 2.875, 0.125),
    (42, 3.0, 0.125),
    (42, 3.125, 0.125),
    (42, 3.25, 0.125),
    (42, 3.375, 0.125),
    (42, 3.5, 0.125),
    (42, 3.625, 0.125),
    (42, 3.75, 0.125),
    (42, 3.875, 0.125),
    (42, 4.0, 0.125),
    (42, 4.125, 0.125),
    (42, 4.25, 0.125),
    (42, 4.375, 0.125),
    (42, 4.5, 0.125),
    (42, 4.625, 0.125),
    (42, 4.75, 0.125),
    (42, 4.875, 0.125),
    (42, 5.0, 0.125),
    (42, 5.125, 0.125),
    (42, 5.25, 0.125),
    (42, 5.375, 0.125),
    (42, 5.5, 0.125),
    (42, 5.625, 0.125),
    (42, 5.75, 0.125),
    (42, 5.875, 0.125)
]
for note, start, duration in hi_hat_notes:
    h = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(h)

# Add kick and snare in bars 2-4
kick_notes = [
    (36, 1.5, 0.375),
    (36, 2.25, 0.375),
    (36, 3.0, 0.375),
    (36, 3.75, 0.375),
    (36, 4.5, 0.375)
]
for note, start, duration in kick_notes:
    k = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(k)

snare_notes = [
    (38, 1.875, 0.375),
    (38, 2.625, 0.375),
    (38, 3.375, 0.375),
    (38, 4.125, 0.375),
    (38, 4.875, 0.375)
]
for note, start, duration in snare_notes:
    s = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(s)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
