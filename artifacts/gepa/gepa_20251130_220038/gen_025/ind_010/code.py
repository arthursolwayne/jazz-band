
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),   # G#
    
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),   # C
    
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=6.0),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),   # C
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=1.875),   # E
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),   # G
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),   # Bb
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),   # E
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),   # Bb
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),   # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, one phrase, leave it hanging, come back and finish
# F - G - Bb - C (start on beat 2, end on beat 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.125, end=2.5),    # C
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.875),    # E
    pretty_midi.Note(velocity=100, pitch=52, start=2.875, end=3.0),    # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add fill at end of bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=5.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=5.875, end=6.0),    # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
