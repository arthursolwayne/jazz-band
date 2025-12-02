
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2 (1.5 - 3.0s): Full quartet
# Sax: Motif - D (D4), F# (F#4), B (B4), D (D5)
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (66, 1.875, 0.375), # F#4
    (67, 2.25, 0.375),  # B4
    (72, 2.625, 0.375)  # D5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in D minor
bass_notes = [
    (45, 1.5, 0.375),  # D3
    (47, 1.875, 0.375), # F#3
    (49, 2.25, 0.375),  # A3
    (45, 2.625, 0.375)  # D3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 1.875, 0.375),  # D7 (D, F#, A, C#)
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (69, 1.875, 0.375),
    (62, 2.625, 0.375),  # D7 again on beat 4
    (64, 2.625, 0.375),
    (67, 2.625, 0.375),
    (69, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3 (3.0 - 4.5s): Sax continues motif, others repeat
# Sax: Repeat same motif but with a slight variation
sax_notes = [
    (62, 3.0, 0.375),  # D4
    (66, 3.375, 0.375), # F#4
    (67, 3.75, 0.375),  # B4
    (72, 4.125, 0.375)  # D5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line continues
bass_notes = [
    (47, 3.0, 0.375),  # F#3
    (49, 3.375, 0.375), # A3
    (50, 3.75, 0.375),  # Bb3
    (47, 4.125, 0.375)  # F#3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 again
piano_notes = [
    (62, 3.375, 0.375),  # D7
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (69, 3.375, 0.375),
    (62, 4.125, 0.375),  # D7
    (64, 4.125, 0.375),
    (67, 4.125, 0.375),
    (69, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Same pattern
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5, end=start + 1.5 + duration))

# Bar 4 (4.5 - 6.0s): Sax resolves motif, others continue
# Sax: Resolve to D
sax_notes = [
    (62, 4.5, 0.75)  # D4 held
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line continues
bass_notes = [
    (50, 4.5, 0.375),  # Bb3
    (47, 4.875, 0.375), # F#3
    (49, 5.25, 0.375),  # A3
    (45, 5.625, 0.375)  # D3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on beat 2
piano_notes = [
    (62, 4.875, 0.375),  # D7
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (69, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Same pattern
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 3.0, end=start + 3.0 + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
