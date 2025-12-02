
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
    
    # Bar 2
    (38, 1.875, 0.375), (36, 2.25, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875),
    
    # Bar 3
    (36, 3.375, 0.375), (38, 3.75, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875), (42, 4.5, 0.1875),
    
    # Bar 4
    (38, 4.875, 0.375), (36, 5.25, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875), (42, 6.0, 0.1875)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (Dm7)
    (50, 1.5, 0.375), (49, 1.875, 0.375), (51, 2.25, 0.375), (50, 2.625, 0.375),
    # Bar 3 (Dm7)
    (48, 3.0, 0.375), (47, 3.375, 0.375), (49, 3.75, 0.375), (48, 4.125, 0.375),
    # Bar 4 (Dm7)
    (50, 4.5, 0.375), (49, 4.875, 0.375), (51, 5.25, 0.375), (50, 5.625, 0.375)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (Dm7)
    (62, 1.875, 0.1875), (67, 1.875, 0.1875), (69, 1.875, 0.1875), (64, 1.875, 0.1875),
    # Bar 3 (Dm7)
    (62, 3.375, 0.1875), (67, 3.375, 0.1875), (69, 3.375, 0.1875), (64, 3.375, 0.1875),
    # Bar 4 (Dm7)
    (62, 4.875, 0.1875), (67, 4.875, 0.1875), (69, 4.875, 0.1875), (64, 4.875, 0.1875)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (62, 1.5, 0.1875), (65, 1.6875, 0.1875), (62, 1.875, 0.1875),
    # Bar 3
    (65, 3.0, 0.1875), (67, 3.1875, 0.1875), (65, 3.375, 0.1875),
    # Bar 4
    (64, 4.5, 0.1875), (62, 4.6875, 0.1875), (65, 4.875, 0.1875), (64, 5.0625, 0.1875)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
