
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
    # Bar 1: 0.0 - 1.5s
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on 2
    (42, 0.375, 0.1875),  # Hihat on 3
    (42, 0.5625, 0.1875),  # Hihat on 4
    (36, 0.75, 0.375),  # Kick on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on 4
    (42, 1.125, 0.1875),  # Hihat on 5
    (42, 1.3125, 0.1875)  # Hihat on 6
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif in D minor, start on D (62), ascend to F# (66), resolve back to D
# Bars 2-4: sax melody
sax_notes = [
    (62, 1.5, 0.375),  # D
    (66, 1.875, 0.375),  # F#
    (62, 2.25, 0.375),  # D
    (62, 2.625, 0.375),  # D
    (66, 2.625, 0.375),  # F#
    (62, 2.625, 0.375),  # D
    (62, 3.0, 0.375)    # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in D minor, chromatic passing tones
bass_notes = [
    (58, 1.5, 0.375),  # C
    (60, 1.875, 0.375),  # D
    (59, 2.25, 0.375),  # C#
    (62, 2.625, 0.375),  # D
    (60, 3.0, 0.375),  # D
    (58, 3.375, 0.375),  # C
    (60, 3.75, 0.375),  # D
    (59, 4.125, 0.375),  # C#
    (62, 4.5, 0.375),  # D
    (60, 4.875, 0.375),  # D
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp in D minor
piano_notes = [
    # Bar 2, beat 2: Dm7 (62, 64, 65, 67)
    (67, 1.875, 0.375),  # B
    (65, 1.875, 0.375),  # F
    (64, 1.875, 0.375),  # D
    (62, 1.875, 0.375),  # C
    # Bar 2, beat 4: Dm7 again
    (67, 2.625, 0.375),  # B
    (65, 2.625, 0.375),  # F
    (64, 2.625, 0.375),  # D
    (62, 2.625, 0.375),  # C
    # Bar 3, beat 2: Dm7 again
    (67, 3.375, 0.375),  # B
    (65, 3.375, 0.375),  # F
    (64, 3.375, 0.375),  # D
    (62, 3.375, 0.375),  # C
    # Bar 3, beat 4: Dm7 again
    (67, 4.125, 0.375),  # B
    (65, 4.125, 0.375),  # F
    (64, 4.125, 0.375),  # D
    (62, 4.125, 0.375),  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Drums repeat same pattern
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.0, 0.1875),  # Hihat on 1
    (42, 3.1875, 0.1875),  # Hihat on 2
    (42, 3.375, 0.1875),  # Hihat on 3
    (42, 3.5625, 0.1875),  # Hihat on 4
    (36, 3.75, 0.375),  # Kick on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 3.75, 0.1875),  # Hihat on 3
    (42, 3.9375, 0.1875),  # Hihat on 4
    (42, 4.125, 0.1875),  # Hihat on 5
    (42, 4.3125, 0.1875)  # Hihat on 6
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Drums repeat same pattern
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875),  # Hihat on 2
    (42, 4.875, 0.1875),  # Hihat on 3
    (42, 5.0625, 0.1875),  # Hihat on 4
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.25, 0.1875),  # Hihat on 3
    (42, 5.4375, 0.1875),  # Hihat on 4
    (42, 5.625, 0.1875),  # Hihat on 5
    (42, 5.8125, 0.1875)  # Hihat on 6
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Sax continues the motif with a slight variation
sax_notes = [
    (62, 4.5, 0.375),  # D
    (66, 4.875, 0.375),  # F#
    (62, 5.25, 0.375),  # D
    (62, 5.625, 0.375),  # D
    (66, 5.625, 0.375),  # F#
    (62, 5.625, 0.375),  # D
    (62, 6.0, 0.375)    # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line continues
bass_notes = [
    (60, 4.5, 0.375),  # D
    (58, 4.875, 0.375),  # C
    (60, 5.25, 0.375),  # D
    (59, 5.625, 0.375),  # C#
    (62, 6.0, 0.375),  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 for bar 4
piano_notes = [
    (67, 4.875, 0.375),  # B
    (65, 4.875, 0.375),  # F
    (64, 4.875, 0.375),  # D
    (62, 4.875, 0.375),  # C
    (67, 5.625, 0.375),  # B
    (65, 5.625, 0.375),  # F
    (64, 5.625, 0.375),  # D
    (62, 5.625, 0.375),  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
