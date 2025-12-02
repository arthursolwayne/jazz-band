
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
    (36, 0.0, 0.375),  # Kick on beat 1
    (42, 0.0, 0.1875), # Hihat on 1 & 1/8
    (42, 0.1875, 0.1875), # Hihat on 1/2
    (38, 0.375, 0.375), # Snare on beat 2
    (42, 0.375, 0.1875), # Hihat on 2 & 1/8
    (42, 0.5625, 0.1875), # Hihat on 2/2
    (36, 0.75, 0.375),  # Kick on beat 3
    (42, 0.75, 0.1875), # Hihat on 3 & 1/8
    (42, 0.9375, 0.1875), # Hihat on 3/2
    (38, 1.125, 0.375), # Snare on beat 4
    (42, 1.125, 0.1875), # Hihat on 4 & 1/8
    (42, 1.3125, 0.1875) # Hihat on 4/2
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: chromatic walking line in F minor
bass_notes = [
    (48, 1.5, 0.375),  # F
    (49, 1.875, 0.375), # Gb
    (50, 2.25, 0.375),  # G
    (51, 2.625, 0.375), # Ab
    (53, 2.625, 0.375), # Bb
    (55, 3.0, 0.375),   # B
    (57, 3.375, 0.375), # C
    (58, 3.75, 0.375),  # C#
    (59, 4.125, 0.375), # D
    (60, 4.5, 0.375),   # D#
    (62, 4.875, 0.375), # F
    (64, 5.25, 0.375)   # F#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - Diane: 7th chords on 2 and 4, comp on offbeats
piano_notes = [
    # Bar 2
    (62, 1.5, 0.1875), # F7: F, A, C, Eb (F)
    (69, 1.5, 0.1875), # F7: A
    (64, 1.5, 0.1875), # F7: C
    (60, 1.5, 0.1875), # F7: Eb
    (65, 1.875, 0.1875), # G7: G
    (72, 1.875, 0.1875), # G7: B
    (67, 1.875, 0.1875), # G7: D
    (63, 1.875, 0.1875), # G7: F
    # Bar 3
    (62, 2.25, 0.1875), # F7: F
    (69, 2.25, 0.1875), # F7: A
    (64, 2.25, 0.1875), # F7: C
    (60, 2.25, 0.1875), # F7: Eb
    (65, 2.625, 0.1875), # G7: G
    (72, 2.625, 0.1875), # G7: B
    (67, 2.625, 0.1875), # G7: D
    (63, 2.625, 0.1875), # G7: F
    # Bar 4
    (62, 3.0, 0.1875), # F7: F
    (69, 3.0, 0.1875), # F7: A
    (64, 3.0, 0.1875), # F7: C
    (60, 3.0, 0.1875), # F7: Eb
    (65, 3.375, 0.1875), # G7: G
    (72, 3.375, 0.1875), # G7: B
    (67, 3.375, 0.1875), # G7: D
    (63, 3.375, 0.1875), # G7: F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Saxophone - Dante: concise motif, emotional, memorable
sax_notes = [
    (66, 1.5, 0.375),  # F
    (67, 1.875, 0.375), # G
    (68, 2.25, 0.375),  # Ab
    (66, 2.625, 0.375), # F
    (69, 3.0, 0.375),   # A
    (67, 3.375, 0.375), # G
    (66, 3.75, 0.375),  # F
    (64, 4.125, 0.375), # D
    (66, 4.5, 0.375),   # F
    (68, 4.875, 0.375), # Ab
    (66, 5.25, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
