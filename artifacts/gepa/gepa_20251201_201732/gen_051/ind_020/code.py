
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bar 2 (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # D2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=40, start=2.125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, different chord each bar
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # C#6
]
piano.notes.extend(piano_notes)

# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E5
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # A5
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # G2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=46, start=3.625, end=4.0),
    pretty_midi.Note(velocity=90, pitch=48, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, different chord each bar
# Bar 3: Bm7 (B-D-F#-A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # B5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # D6
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # F#6
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.5),  # A6
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # A5
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # E5
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # A5
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D5
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # B2 (tonic) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=46, start=5.125, end=5.5),
    pretty_midi.Note(velocity=90, pitch=43, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, different chord each bar
# Bar 4: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # A5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # C#6
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # E5
]
sax.notes.extend(sax_notes)

# Drums: continue with same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
