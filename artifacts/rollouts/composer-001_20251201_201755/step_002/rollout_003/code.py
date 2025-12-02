
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
              pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)]
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
               pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)]
hihat_notes = []
for i in range(4):
    hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=i * 0.375 + 0.1875))
drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (D2) to A2 (A2) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # E2
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625),  # D#2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F#2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875),  # C#5
]
# Bar 3: Bm7 (B-D-F#-A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # F#5
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # A5
])
# Bar 4: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G5
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B5
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D6
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# Bar 2: D4, E4, D#4, F#4 (Melody)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),  # D#4
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # F#4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
              pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5625)]
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
               pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)]
hihat_notes = []
for i in range(6, 8):
    hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=i * 0.375 + 0.1875))
drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# Bar 4: Drums continue
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=3.5625, end=3.75),
              pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125)]
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
               pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)]
hihat_notes = []
for i in range(8, 10):
    hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=i * 0.375 + 0.1875))
drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
