
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)

drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2, drum_hihat, drum_hihat2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano - Diane (7th chords on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=2.0),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=2.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=3.0),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=2.5, end=3.0),  # Eb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.5),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.5),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.5),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=4.0, end=4.5),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=4.0, end=4.5),  # Eb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=5.0),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=5.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=6.0),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=5.5, end=6.0),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=5.5, end=6.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax - Dante (melody: one short motif, start it, leave it hanging, finish it)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=110, pitch=72, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=59, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=110, pitch=57, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=110, pitch=59, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: full bar (1.5 - 6.0s)
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875)
drum_kick5 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0)
drum_kick6 = pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125)
drum_kick7 = pretty_midi.Note(velocity=100, pitch=36, start=5.875, end=6.0)

drum_snare3 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.5)
drum_snare4 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.625)
drum_snare5 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75)
drum_snare6 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.875)

drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=6.0)

drums.notes.extend([drum_kick3, drum_kick4, drum_kick5, drum_kick6, drum_kick7,
                    drum_snare3, drum_snare4, drum_snare5, drum_snare6,
                    drum_hihat3])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
