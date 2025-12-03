
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
drum_notes_bar1 = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5), # Hihat
]
for note in drum_notes_bar1:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes_bar2 = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75), # D2
    pretty_midi.Note(velocity=80, pitch=55, start=1.75, end=2.0), # A2
    pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.25), # C2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5), # D2
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.75), # A2
    pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=3.0), # B2 (chromatic approach)
]
for note in bass_notes_bar2:
    bass.notes.append(note)

# Piano: Open voicings, different chords each bar, resolve on the last
piano_notes_bar2 = [
    # Dm7: D F A C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75), # D4
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75), # F4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75), # A4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75), # C4
    # G7: G B D F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0), # G4
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0), # B4
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0), # D4
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0), # F4
    # Cm7: C Eb G Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25), # C4
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.25), # Eb4
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25), # G4
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25), # Bb4
    # F7: F A C E
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5), # F4
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5), # A4
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5), # C4
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.5), # E4
]
for note in piano_notes_bar2:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.125), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.875), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.875), # Hihat
]
for note in drum_notes_bar2:
    drums.notes.append(note)

# Sax: Tenor motif, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5), # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75), # E4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0), # F4
]
for note in sax_notes_bar2:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes_bar3 = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25), # B2
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5), # C3
    pretty_midi.Note(velocity=80, pitch=59, start=3.5, end=3.75), # B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0), # C3
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25), # D3
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5), # G3 (chromatic approach)
]
for note in bass_notes_bar3:
    bass.notes.append(note)

# Piano: Open voicings, different chords each bar, resolve on the last
piano_notes_bar3 = [
    # Bm7: B D F# A
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25), # B4
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25), # D4
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25), # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25), # A4
    # Cm7: C Eb G Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5), # C4
    pretty_midi.Note(velocity=80, pitch=63, start=3.25, end=3.5), # Eb4
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5), # G4
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5), # Bb4
    # Dm7: D F A C
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75), # D4
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75), # F4
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75), # A4
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75), # C4
    # G7: G B D F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0), # G4
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0), # B4
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0), # D4
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0), # F4
]
for note in piano_notes_bar3:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.625), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.625), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.375), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.375), # Hihat
]
for note in drum_notes_bar3:
    drums.notes.append(note)

# Sax: Continue motif, finish it with a resolution
sax_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0), # A4
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25), # E4
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5), # F4
]
for note in sax_notes_bar3:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes_bar4 = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75), # D3
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0), # G3
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25), # E3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5), # D3
    pretty_midi.Note(velocity=80, pitch=67, start=5.5, end=5.75), # G3
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0), # A3 (chromatic approach)
]
for note in bass_notes_bar4:
    bass.notes.append(note)

# Piano: Open voicings, different chords each bar, resolve on the last
piano_notes_bar4 = [
    # G7: G B D F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75), # G4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75), # B4
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75), # D4
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75), # F4
    # Cm7: C Eb G Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0), # C4
    pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=5.0), # Eb4
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0), # G4
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0), # Bb4
    # F7: F A C E
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.25), # F4
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25), # A4
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25), # C4
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.25), # E4
    # Dm7: D F A C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5), # D4
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5), # F4
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5), # A4
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5), # C4
]
for note in piano_notes_bar4:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.125), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.875), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.875), # Hihat
]
for note in drum_notes_bar4:
    drums.notes.append(note)

# Sax: Motif variation, maintain tension
sax_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0), # A4
]
for note in sax_notes_bar4:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
