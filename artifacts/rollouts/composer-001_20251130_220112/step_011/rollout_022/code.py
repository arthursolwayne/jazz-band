
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

# Bars 2-4: Full quartet

# Bass line (Marcus) - chromatic walking line in D
bass_notes = [
    (62, 1.5, 0.375), # D
    (63, 1.875, 0.375), # Eb
    (64, 2.25, 0.375), # E
    (65, 2.625, 0.375), # F
    (67, 3.0, 0.375), # G
    (69, 3.375, 0.375), # A
    (71, 3.75, 0.375), # B
    (72, 4.125, 0.375), # C
    (69, 4.5, 0.375), # A
    (71, 4.875, 0.375), # B
    (72, 5.25, 0.375), # C
    (67, 5.625, 0.375), # G
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    (62, 1.875, 0.375), # D
    (67, 1.875, 0.375), # G
    (69, 1.875, 0.375), # A
    (64, 1.875, 0.375), # F# (7th)
    # Bar 3: D7 on beat 2
    (62, 3.375, 0.375), # D
    (67, 3.375, 0.375), # G
    (69, 3.375, 0.375), # A
    (64, 3.375, 0.375), # F# (7th)
    # Bar 4: D7 on beat 2
    (62, 4.875, 0.375), # D
    (67, 4.875, 0.375), # G
    (69, 4.875, 0.375), # A
    (64, 4.875, 0.375), # F# (7th)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax (Dante) - motif
sax_notes = [
    (62, 1.5, 0.375), # D (start of motif)
    (64, 1.875, 0.375), # E
    (62, 2.25, 0.375), # D
    (60, 2.625, 0.375), # C
    (62, 3.0, 0.375), # D (return)
    (64, 3.375, 0.375), # E
    (62, 3.75, 0.375), # D
    (60, 4.125, 0.375), # C
    (62, 4.5, 0.375), # D
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375), # D
    (60, 5.625, 0.375), # C
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
