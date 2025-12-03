
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

# Create kick on 1 and 3
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
              pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)]
drums.notes.extend(kick_notes)

# Snare on 2 and 4
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
               pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375)]
drums.notes.extend(snare_notes)

# Hi-hat on every eighth
hihat_notes = []
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Key is F major: F, Gm, Am7, Bbmaj7, Cm7, Dm7, Em7, F7

# Bar 2: F7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=2.75)  # F
]
bass.notes.extend(bass_notes)

# Bar 3: Gm7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=80, pitch=76, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.625),   # F
    pretty_midi.Note(velocity=80, pitch=72, start=3.875, end=4.0)    # G
]
bass.notes.extend(bass_notes)

# Bar 4: Am7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=73, start=4.0, end=4.125),   # A
    pretty_midi.Note(velocity=80, pitch=77, start=4.375, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=73, start=5.125, end=5.25)   # A
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: F7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=6.0)   # G
]
piano.notes.extend(piano_notes)

# Bar 3: Gm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=86, start=1.5, end=6.0)   # A
]
piano.notes.extend(piano_notes)

# Bar 4: Am7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=89, start=1.5, end=6.0)   # C
]
piano.notes.extend(piano_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - E - F (F7 arpeggio with a twist)
# Bar 2: Play first 2 notes
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0)   # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Leave it hanging (no notes)
# Bar 4: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0)   # F
]
sax.notes.extend(sax_notes)

# Add drum fills for bar 2 and 4
# Bar 2: Fill on 3
fill_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),   # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.125),   # Hihat
    pretty_midi.Note(velocity=110, pitch=36, start=2.0, end=2.125)   # Kick
]
drums.notes.extend(fill_notes)

# Bar 4: Fill on 3
fill_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),   # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.125),   # Hihat
    pretty_midi.Note(velocity=110, pitch=36, start=5.0, end=5.125)   # Kick
]
drums.notes.extend(fill_notes)

# Add final note on piano for resolution
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=6.0)  # F
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
