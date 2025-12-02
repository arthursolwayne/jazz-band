
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.5625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeats
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0), # G#
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5), # C
    pretty_midi.Note(velocity=80, pitch=54, start=4.5, end=4.875), # C#
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0), # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0), # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0), # D
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5), # F
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5), # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5), # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5), # D
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0), # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0), # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0), # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0), # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
