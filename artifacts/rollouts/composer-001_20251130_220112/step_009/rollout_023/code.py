
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=3.0),  # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.0),  # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=79, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=81, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=4.75, end=5.0),  # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=86, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=88, start=5.25, end=5.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0),  # G7 again
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=81, start=2.5, end=3.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=4.0),  # G7 again
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=79, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=81, start=3.5, end=4.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=1.75, end=2.0),  # A
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=2.75, end=3.0),  # A
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start+0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start+0.75, end=bar_start+1.125)
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start+0.75)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start+0.75, end=bar_start+1.5)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start+1.125, end=bar_start+1.5)
    dr = [kick, snare, hihat1, hihat2, kick2]
    drums.notes.extend(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_russo_intro.mid')
