
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Dm (F, G, A, Bb, C, D, Eb, D)
bass_notes = [
    (65, 1.5, 0.375), (67, 1.875, 0.375), (69, 2.25, 0.375), (67, 2.625, 0.375),
    (69, 3.0, 0.375), (71, 3.375, 0.375), (69, 3.75, 0.375), (67, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Diane: 7th chords on 2 and 4 (Dm7 on 2, G7 on 4)
piano_notes = [
    # Dm7: D, F, A, C (bar 2, beat 2)
    (62, 2.25, 0.375), (64, 2.25, 0.375), (67, 2.25, 0.375), (69, 2.25, 0.375),
    # G7: G, B, D, F (bar 2, beat 4)
    (67, 2.625, 0.375), (71, 2.625, 0.375), (69, 2.625, 0.375), (64, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Dante: Sax motif (D, Eb, F, G) - short, singable, leaves it hanging
sax_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (64, 2.25, 0.375), (65, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Continue walking bass
bass_notes = [
    (67, 3.0, 0.375), (69, 3.375, 0.375), (71, 3.75, 0.375), (69, 4.125, 0.375),
    (71, 4.5, 0.375), (72, 4.875, 0.375), (71, 5.25, 0.375), (69, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Diane: 7th chords on 2 and 4 (Dm7 on 2, G7 on 4)
piano_notes = [
    # Dm7: D, F, A, C (bar 3, beat 2)
    (62, 3.75, 0.375), (64, 3.75, 0.375), (67, 3.75, 0.375), (69, 3.75, 0.375),
    # G7: G, B, D, F (bar 3, beat 4)
    (67, 4.125, 0.375), (71, 4.125, 0.375), (69, 4.125, 0.375), (64, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875)
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Dante: Continue sax motif (D, Eb, F, G), then lead into the next bar
sax_notes = [
    (62, 3.0, 0.375), (63, 3.375, 0.375), (64, 3.75, 0.375), (65, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Continue walking bass
bass_notes = [
    (69, 4.5, 0.375), (71, 4.875, 0.375), (72, 5.25, 0.375), (71, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Diane: 7th chords on 2 and 4 (Dm7 on 2, G7 on 4)
piano_notes = [
    # Dm7: D, F, A, C (bar 4, beat 2)
    (62, 5.25, 0.375), (64, 5.25, 0.375), (67, 5.25, 0.375), (69, 5.25, 0.375),
    # G7: G, B, D, F (bar 4, beat 4)
    (67, 5.625, 0.375), (71, 5.625, 0.375), (69, 5.625, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Dante: Complete the motif and end with a G (resolution)
sax_notes = [
    (62, 4.5, 0.375), (63, 4.875, 0.375), (64, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
