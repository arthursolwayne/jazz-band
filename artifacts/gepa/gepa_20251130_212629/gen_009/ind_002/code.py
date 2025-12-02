
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375), # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bassline in Fm (F, Ab, Bb, Db)
# Walking line, chromatic approaches
bass_notes = [
    (64, 1.5, 0.375),   # F
    (62, 1.875, 0.375),  # Eb (chromatic approach to Ab)
    (62, 2.25, 0.375),   # Ab
    (60, 2.625, 0.375),  # G (chromatic approach to Bb)
    (60, 2.875, 0.375),  # Bb
    (58, 3.25, 0.375),   # Ab (chromatic approach to Db)
    (58, 3.625, 0.375),  # Db
    (56, 4.0, 0.375),    # C (chromatic approach to F)
    (56, 4.375, 0.375),  # F
    (54, 4.75, 0.375),   # Eb (chromatic approach to Ab)
    (54, 5.125, 0.375),  # Ab
    (52, 5.5, 0.375),    # G (chromatic approach to Bb)
    (51, 5.875, 0.375),  # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane - Piano: 7th chords, comp on 2 and 4
# In Fm7 (F, Ab, Bb, Db)
piano_notes = [
    # Bar 2: F7 on beat 2
    (64, 2.25, 0.375),   # F
    (69, 2.25, 0.375),   # Ab
    (71, 2.25, 0.375),   # Bb
    (67, 2.25, 0.375),   # Db
    # Bar 3: F7 on beat 2
    (64, 3.25, 0.375),
    (69, 3.25, 0.375),
    (71, 3.25, 0.375),
    (67, 3.25, 0.375),
    # Bar 4: F7 on beat 2
    (64, 4.25, 0.375),
    (69, 4.25, 0.375),
    (71, 4.25, 0.375),
    (67, 4.25, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Drums continue (full bar)
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5, end=start + 1.5 + duration))

# Dante - Tenor sax: One short motif, make it sing
# Fm7 -> Ab7 -> Bb7 -> F7 (Motif)
# Start on F, then Ab, then Bb, then F (hanging)
sax_notes = [
    (64, 1.5, 0.375),   # F
    (68, 1.875, 0.375),  # Ab
    (71, 2.25, 0.375),   # Bb
    (64, 2.625, 0.375),  # F (hanging)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
