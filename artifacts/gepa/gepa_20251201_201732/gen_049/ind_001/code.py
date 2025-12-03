
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
    (36, 0.0, 1.0), (38, 0.5, 1.0), (42, 0.0, 1.0),
    (36, 1.0, 1.0), (38, 1.5, 1.0), (42, 1.0, 1.0)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375), (40, 1.875, 0.375), (41, 2.25, 0.375), (43, 2.625, 0.375),  # F2, G2#, G3, A3
    (38, 3.0, 0.375), (40, 3.375, 0.375), (41, 3.75, 0.375), (43, 4.125, 0.375),  # F2, G2#, G3, A3
    (38, 4.5, 0.375), (40, 4.875, 0.375), (41, 5.25, 0.375), (43, 5.625, 0.375),  # F2, G2#, G3, A3
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (53, 1.5, 0.5), (57, 1.5, 0.5), (60, 1.5, 0.5), (63, 1.5, 0.5),  # F, Ab, C, Eb
    (53, 2.0, 0.5), (57, 2.0, 0.5), (60, 2.0, 0.5), (63, 2.0, 0.5),  # F, Ab, C, Eb
    (53, 2.5, 0.5), (57, 2.5, 0.5), (60, 2.5, 0.5), (63, 2.5, 0.5),  # F, Ab, C, Eb
    (53, 3.0, 0.5), (57, 3.0, 0.5), (60, 3.0, 0.5), (63, 3.0, 0.5),  # F, Ab, C, Eb
]
# Bar 3: Bb7 (Bb, D, F, Ab)
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    (60, 3.5, 0.5), (63, 3.5, 0.5), (67, 3.5, 0.5), (67, 4.0, 0.5),  # C, Eb, G, Bb
    (60, 4.0, 0.5), (63, 4.0, 0.5), (67, 4.0, 0.5), (67, 4.5, 0.5),  # C, Eb, G, Bb
    (60, 4.5, 0.5), (63, 4.5, 0.5), (67, 4.5, 0.5), (67, 5.0, 0.5),  # C, Eb, G, Bb
    (60, 5.0, 0.5), (63, 5.0, 0.5), (67, 5.0, 0.5), (67, 5.5, 0.5),  # C, Eb, G, Bb
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax: One short motif, start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, G, F (MIDI 53, 57, 67, 53)
sax_notes = [
    (53, 1.5, 0.5), (57, 1.75, 0.5), (67, 2.0, 0.5), (53, 2.5, 0.5),  # First pass
    (53, 3.5, 0.5), (57, 3.75, 0.5), (67, 4.0, 0.5), (53, 4.5, 0.5),  # Second pass
    (53, 5.5, 0.5)  # Final resolution
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
