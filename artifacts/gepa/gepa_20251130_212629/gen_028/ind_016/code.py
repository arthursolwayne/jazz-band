
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums, with a sparse groove that sets the mood

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat 1
    (42, 0.1875, 0.1875),# Hihat 2
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat 2
    (42, 0.5625, 0.1875),# Hihat 3
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat 3
    (42, 0.9375, 0.1875),# Hihat 4
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875), # Hihat 4
    (42, 1.3125, 0.1875) # Hihat 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Sax enters with a short, lyrical motif (1.5 - 3.0s)
# Dm7 (D F A C) -> D F A C
# Phrasing: start on beat 1, end before beat 3, leave it hanging

# Bar 2: 1.5 - 3.0s
sax_notes = [
    (62, 1.5, 0.375),    # D (beat 1)
    (64, 1.875, 0.375),  # F (beat 2.5)
    (67, 2.25, 0.375),   # A (beat 3)
    (69, 2.625, 0.375),  # C (beat 3.5)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 2: Bass line (walking line with chromatic approaches)
bass_notes = [
    (62, 1.5, 0.375),    # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),   # F
    (65, 2.625, 0.375),  # G
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Bar 2: Piano (7th chords on 2 and 4)
piano_notes = [
    (62, 1.875, 0.375),  # D7 (D F A C)
    (62, 1.875, 0.375),
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (69, 2.625, 0.375),
    (69, 2.625, 0.375),
    (71, 2.625, 0.375),
    (72, 2.625, 0.375),
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Sax continues the motif (3.0 - 4.5s)
# Rest on beat 1, then echo the motif with a slight variation

sax_notes = [
    (0, 3.0, 0.375),     # Rest
    (64, 3.375, 0.375),  # F
    (67, 3.75, 0.375),   # A
    (69, 4.125, 0.375),  # C
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 3: Bass line continues the walking line
bass_notes = [
    (62, 3.0, 0.375),    # D
    (63, 3.375, 0.375),  # Eb
    (64, 3.75, 0.375),   # F
    (65, 4.125, 0.375),  # G
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Bar 3: Piano continues with 7th chords on 2 and 4
piano_notes = [
    (62, 3.375, 0.375),
    (62, 3.375, 0.375),
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (69, 4.125, 0.375),
    (69, 4.125, 0.375),
    (71, 4.125, 0.375),
    (72, 4.125, 0.375),
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Drums continue (same pattern)
drum_notes = [
    (36, 3.0, 0.375),
    (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875),
    (38, 3.375, 0.375),
    (42, 3.375, 0.1875),
    (42, 3.5625, 0.1875),
    (36, 3.75, 0.375),
    (42, 3.75, 0.1875),
    (42, 3.9375, 0.1875),
    (38, 4.125, 0.375),
    (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Sax resolves with a question (4.5 - 6.0s)
# End on a suspended note, not a resolution

sax_notes = [
    (62, 4.5, 0.375),    # D (beat 1)
    (64, 4.875, 0.375),  # F (beat 2.5)
    (67, 5.25, 0.375),   # A (beat 3)
    (64, 5.625, 0.375),  # F (beat 3.5) - left hanging
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 4: Bass continues the walking line
bass_notes = [
    (62, 4.5, 0.375),    # D
    (63, 4.875, 0.375),  # Eb
    (64, 5.25, 0.375),   # F
    (65, 5.625, 0.375),  # G
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Bar 4: Piano continues with 7th chords on 2 and 4
piano_notes = [
    (62, 4.875, 0.375),
    (62, 4.875, 0.375),
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (69, 5.625, 0.375),
    (69, 5.625, 0.375),
    (71, 5.625, 0.375),
    (72, 5.625, 0.375),
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Drums continue
drum_notes = [
    (36, 4.5, 0.375),
    (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875),
    (38, 4.875, 0.375),
    (42, 4.875, 0.1875),
    (42, 5.0625, 0.1875),
    (36, 5.25, 0.375),
    (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875),
    (38, 5.625, 0.375),
    (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
