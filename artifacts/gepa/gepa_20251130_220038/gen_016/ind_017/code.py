
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

# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=end).add_to_parent(drums)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# D minor scale: D, Eb, F, G, Ab, Bb, B
# Bar 2 (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Bar 3 (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # B
]
bass.notes.extend(bass_notes)

# Bar 4 (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D, F, Ab, C
# Bar 2 (1.5 - 3.0s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # C
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # C
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 scale: D, Eb, F, G, Ab, Bb, B
# Motif: D, G, Bb -> leave it hanging on Bb, then come back with D

# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick_start = start
    kick_end = start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end).add_to_parent(drums)
    kick_start = start + 1.125
    kick_end = kick_start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end).add_to_parent(drums)

# Snare on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    snare_start = start + 0.75
    snare_end = snare_start + 0.375
    pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end).add_to_parent(drums)
    snare_start = start + 1.875
    snare_end = snare_start + 0.375
    pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end).add_to_parent(drums)

# Hi-hat on every eighth
for i in range(4, 12):
    start = i * 0.375
    end = start + 0.375
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=end).add_to_parent(drums)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
