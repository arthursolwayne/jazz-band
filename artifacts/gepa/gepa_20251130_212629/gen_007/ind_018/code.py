
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
    
    (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (59, 1.5, 0.375), (60, 1.875, 0.375), (58, 2.25, 0.375), (62, 2.625, 0.375),  # Dm7 walk
    (60, 3.0, 0.375),
    
    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 0.375), (63, 3.375, 0.375), (61, 3.75, 0.375), (65, 4.125, 0.375),  # Dm7 walk
    (63, 4.5, 0.375),
    
    # Bar 4 (4.5 - 6.0s)
    (63, 4.5, 0.375), (64, 4.875, 0.375), (62, 5.25, 0.375), (66, 5.625, 0.375),  # Dm7 walk
    (64, 6.0, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.875, 0.375), (67, 1.875, 0.375), (60, 1.875, 0.375), (64, 1.875, 0.375),  # Dm7
    (62, 3.0, 0.375), (67, 3.0, 0.375), (60, 3.0, 0.375), (64, 3.0, 0.375),  # Dm7
    
    # Bar 3 (3.0 - 4.5s)
    (62, 3.375, 0.375), (67, 3.375, 0.375), (60, 3.375, 0.375), (64, 3.375, 0.375),  # Dm7
    (62, 4.5, 0.375), (67, 4.5, 0.375), (60, 4.5, 0.375), (64, 4.5, 0.375),  # Dm7
    
    # Bar 4 (4.5 - 6.0s)
    (62, 4.875, 0.375), (67, 4.875, 0.375), (60, 4.875, 0.375), (64, 4.875, 0.375),  # Dm7
    (62, 6.0, 0.375), (67, 6.0, 0.375), (60, 6.0, 0.375), (64, 6.0, 0.375)  # Dm7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375),  # F
    (64, 2.25, 0.375),  # E
    (62, 2.625, 0.375),  # D
    
    # Bar 3 (3.0 - 4.5s)
    (64, 3.0, 0.375),  # E
    (67, 3.375, 0.375),  # G
    (65, 3.75, 0.375),  # F
    (64, 4.125, 0.375),  # E
    
    # Bar 4 (4.5 - 6.0s)
    (64, 4.5, 0.375),  # E
    (67, 4.875, 0.375),  # G
    (65, 5.25, 0.375),  # F
    (62, 5.625, 0.375)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
