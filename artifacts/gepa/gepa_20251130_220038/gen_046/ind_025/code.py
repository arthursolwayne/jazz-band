
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on 2
    (42, 0.375, 0.1875),  # Hihat on 3
    (42, 0.5625, 0.1875), # Hihat on 4
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),   # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 3
    (42, 1.3125, 0.1875), # Hihat on 4
    (42, 1.5, 0.1875)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (Bass): Walking line, chromatic approaches, no repeating notes
bass_notes = [
    (37, 1.5, 0.375),  # F (37)
    (38, 1.875, 0.375), # Gb (38)
    (39, 2.25, 0.375),  # G (39)
    (40, 2.625, 0.375), # Ab (40)
    (41, 3.0, 0.375),   # A (41)
    (42, 3.375, 0.375), # Bb (42)
    (43, 3.75, 0.375),  # B (43)
    (44, 4.125, 0.375), # C (44)
    (45, 4.5, 0.375),   # C# (45)
    (46, 4.875, 0.375), # D (46)
    (47, 5.25, 0.375),  # Eb (47)
    (48, 5.625, 0.375)  # E (48)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane (Piano): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb) on 2 and 4
    (53, 1.875, 0.375), # F (53)
    (58, 1.875, 0.375), # A (58)
    (57, 1.875, 0.375), # C (57)
    (60, 1.875, 0.375), # Eb (60)

    (53, 2.625, 0.375), # F (53)
    (58, 2.625, 0.375), # A (58)
    (57, 2.625, 0.375), # C (57)
    (60, 2.625, 0.375), # Eb (60)

    # Bar 3: Bb7 (Bb, D, F, Ab) on 2 and 4
    (59, 3.375, 0.375), # Bb (59)
    (62, 3.375, 0.375), # D (62)
    (57, 3.375, 0.375), # F (57)
    (60, 3.375, 0.375), # Ab (60)

    (59, 4.125, 0.375), # Bb (59)
    (62, 4.125, 0.375), # D (62)
    (57, 4.125, 0.375), # F (57)
    (60, 4.125, 0.375), # Ab (60)

    # Bar 4: C7 (C, E, G, Bb) on 2 and 4
    (57, 4.875, 0.375), # C (57)
    (64, 4.875, 0.375), # E (64)
    (60, 4.875, 0.375), # G (60)
    (62, 4.875, 0.375), # Bb (62)

    (57, 5.625, 0.375), # C (57)
    (64, 5.625, 0.375), # E (64)
    (60, 5.625, 0.375), # G (60)
    (62, 5.625, 0.375)  # Bb (62)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante (Sax): Whisper to cry, motif starts at bar 2
sax_notes = [
    # Bar 2: F (62) - start, leave it hanging
    (62, 1.5, 0.375),

    # Bar 3: Bb (61) - build tension
    (61, 3.0, 0.375),

    # Bar 4: C (60) - resolution, but with a twist
    (60, 5.25, 0.375),

    # Return to F (62) in the next bar
    (62, 5.625, 0.375)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
